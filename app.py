import gradio as gr
import torch
from transformers import MarianMTModel, MarianTokenizer

# 1. Load Model (ID -> EN dan EN -> DE)
MODEL_ID_EN = "Helsinki-NLP/opus-mt-id-en"
MODEL_EN_DE = "Helsinki-NLP/opus-mt-en-de"

tokenizer_id_en = MarianTokenizer.from_pretrained(MODEL_ID_EN)
model_id_en = MarianMTModel.from_pretrained(MODEL_ID_EN)

tokenizer_en_de = MarianTokenizer.from_pretrained(MODEL_EN_DE)
model_en_de = MarianMTModel.from_pretrained(MODEL_EN_DE)

# Gunakan CPU jika di Hugging Face Space gratisan
device = "cuda" if torch.cuda.is_available() else "cpu"
model_id_en = model_id_en.to(device)
model_en_de = model_en_de.to(device)

# 2. Fungsi Logika Translasi
def _run_model(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
    with torch.no_grad():
        tokens = model.generate(**inputs, max_length=512, num_beams=4, early_stopping=True, no_repeat_ngram_size=3)
    return tokenizer.decode(tokens[0], skip_special_tokens=True)

def translate(text: str) -> str:
    text = text.strip()
    if not text:
        return "Input kosong. Silakan masukkan teks terlebih dahulu."
    if len(text) > 2000:
        return "Teks terlalu panjang (maks. 2000 karakter)."
    
    english = _run_model(text, tokenizer_id_en, model_id_en)
    german = _run_model(english, tokenizer_en_de, model_en_de)
    return german

# 3. Pengaturan Tampilan UI (Gradio)
custom_css = """
.gradio-container { font-family: 'Segoe UI', sans-serif; max-width: 900px !important; margin: auto !important; }
.title-text { text-align: center; font-size: 2rem; font-weight: 700; margin-bottom: 0.2rem; }
.subtitle-text { text-align: center; color: #666; font-size: 0.95rem; margin-bottom: 1.5rem; }
.translate-btn { background: linear-gradient(135deg, #c8102e, #ffcc00) !important; color: white !important; font-size: 1rem !important; font-weight: 600 !important; border-radius: 8px !important; padding: 12px !important; }
"""

EXAMPLES = [
    ["Selamat pagi! Apa kabar?"],
    ["Saya ingin memesan secangkir kopi."],
    ["Di mana stasiun kereta terdekat?"],
    ["Indonesia adalah negara kepulauan terbesar di dunia."]
]

def hitung_karakter(text):
    n = len(text)
    warna = "green" if n <= 1500 else ("orange" if n <= 2000 else "red")
    return f"<span style='color:{warna}'>{n}/2000 karakter</span>"

# Menghapus parameter 'css' dari constructor Blocks agar sesuai standar Gradio 6.0
with gr.Blocks(title="Translator Indonesia → Jerman") as demo:
    gr.HTML("<div class='title-text'>🇮🇩 ➡️ 🇩🇪 Translator Indonesia–Jerman</div>")
    gr.HTML("<div class='subtitle-text'>Powered by Helsinki-NLP · HuggingFace Spaces</div>")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### ✍️ Teks Bahasa Indonesia")
            # Menghapus 'show_copy_button=True' yang tidak kompatibel
            input_text = gr.Textbox(placeholder="Ketik kalimat di sini...", lines=8, label="")
            char_count = gr.HTML("<span style='color:gray'>0/2000 karakter</span>")
            input_text.change(fn=hitung_karakter, inputs=input_text, outputs=char_count)
            
        with gr.Column():
            gr.Markdown("### 🇩🇪 Hasil Terjemahan (Deutsch)")
            # Menghapus 'show_copy_button=True' yang tidak kompatibel
            output_text = gr.Textbox(lines=8, interactive=False, label="")

    with gr.Row():
        clear_btn = gr.Button("🗑️ Reset", variant="secondary")
        translate_btn = gr.Button("🔁 Terjemahkan", variant="primary", elem_classes="translate-btn")

    gr.Markdown("--- \n ### 💡 Contoh Kalimat")
    gr.Examples(examples=EXAMPLES, inputs=input_text)

    translate_btn.click(fn=translate, inputs=input_text, outputs=output_text)
    input_text.submit(fn=translate, inputs=input_text, outputs=output_text)
    clear_btn.click(fn=lambda: ("", ""), inputs=None, outputs=[input_text, output_text])

if __name__ == "__main__":
    # Memindahkan parameter custom_css ke dalam method launch() sesuai aturan Gradio 6.0
    demo.launch(css=custom_css)
