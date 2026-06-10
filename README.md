# 🇮🇩 ➡️ 🇩🇪 Machine Translator: Indonesia ke Jerman

Proyek ini adalah aplikasi *Machine Translation* mandiri dari Bahasa Indonesia ke Bahasa Jerman berbasis *Deep Learning* (Natural Language Processing). Aplikasi ini memanfaatkan model *pre-trained* berbasis arsitektur Transformer (**MarianMT**) dari Helsinki-NLP yang di-host di Hugging Face Hub, serta dilengkapi dengan antarmuka web interaktif menggunakan Gradio.

---

## Fitur Utama

* **Pipeline 2-Langkah Translation**
  Menerjemahkan dari **Indonesia ➝ Inggris ➝ Jerman** untuk meningkatkan akurasi dan konteks, menggunakan model:

  * `opus-mt-id-en`
  * `opus-mt-en-de`

* **Antarmuka Web Interaktif**
  Dibangun dengan **Gradio**, memungkinkan pengguna mengetik dan langsung melihat hasil terjemahan secara real-time.

* **Fitur Hitung Karakter**
  Input dibatasi hingga **2000 karakter** dengan indikator visual untuk menjaga efisiensi runtime.

* **Evaluasi BLEU Score**
  Dilengkapi evaluasi kuantitatif menggunakan **sacrebleu** untuk mengukur kualitas terjemahan dibanding referensi manusia.

---

## Struktur Repositori

```
.
├── app.py                         # Aplikasi utama (Gradio UI)
├── translator_indo_jerman.ipynb   # Notebook eksperimen & evaluasi
├── requirements.txt               # Daftar dependensi
└── README.md                      # Dokumentasi proyek
```

---

## Cara Menjalankan Secara Lokal

### 1. Prasyarat

* Python **3.9+**
* pip (package manager Python)

---

### 2. Clone Repository

```bash
git clone https://github.com/username-kamu/nama-repositori-kamu.git
cd nama-repositori-kamu
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Jalankan Aplikasi

```bash
python app.py
```

Setelah berhasil dijalankan, buka browser dan akses:

```
http://127.0.0.1:7860
```

---

## Live Demo

Aplikasi ini telah dideploy di **Hugging Face Spaces** dan dapat diakses secara publik:

**[Coba Aplikasi Translator](#)**
*(https://huggingface.co/spaces/yusri22/Translator_Machine)*

---

## Teknologi yang Digunakan

* Transformer Model (MarianMT)
* Hugging Face Transformers
* Gradio (Web Interface)
* SacreBLEU (Evaluation)
* Python

---

## Catatan

* Pipeline dua tahap digunakan untuk meningkatkan kualitas hasil terjemahan dibanding direct translation.
* Model yang digunakan bersifat pre-trained tanpa fine-tuning tambahan.

---

## Kredit

* Model ID ➝ EN: `Helsinki-NLP/opus-mt-id-en`
* Model EN ➝ DE: `Helsinki-NLP/opus-mt-en-de`
* Framework UI: Gradio
* Lingkungan eksperimen: Google Colab (GPU T4)

---

## Kontak

Jika ada pertanyaan atau kolaborasi, silakan hubungi melalui GitHub atau platform lainnya.

---

⭐ Jangan lupa kasih *star* jika proyek ini bermanfaat!
