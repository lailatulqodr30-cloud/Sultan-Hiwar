# Sultan Hiwar: Chatbot Pembelajaran Maharah Kalam Berbasis AI (Tingkat Menengah)

Proyek ini merupakan implementasi chatbot cerdas berbasis kecerdasan buatan (AI) bernama **Sultan Hiwar** yang dirancang khusus untuk membantu pembelajar Bahasa Arab tingkat menengah (*Mustawa Mutawassit / Intermediate*) dalam melatih Keterampilan Berbicara (**Maharah Kalam**). 

Proyek ini dibangun menggunakan bahasa pemrograman Python dan diintegrasikan dengan Google Gemini API untuk memenuhi tugas proyek **Ujian Akhir Semester (UAS)** pada Program Studi Pendidikan Bahasa Arab (PBA), Semester 6.

---

## 👤 Identitas Mahasiswa
* **Nama Lengkap:** SITI LAILATUL KODARIYAH
* **NIM:** [1232030118]
* **Program Studi:** Pendidikan Bahasa Arab (PBA)
* **Semester / Kelas:** 6 / D (PBA 6D)
* **Instansi:** Universitas Islam Negeri (UIN) Sunan Gunung Djati Bandung

---

## 🎯 Fokus Keterampilan & Level Target

* **Fokus Utama:** Keterampilan Berbicara (**Maharah Kalam** / مَهَارَةُ الْكَلَامِ)
* **Level Pengguna:** Tingkat Menengah (**Mustawa Mutawassit** / المُسْتَوَى المُتَوَسِّط)
* **Alasan Pemilihan Maharah & Level:** Pada tingkat menengah (*intermediate*), pembelajar Bahasa Arab umumnya telah menguasai kosakata dasar (*mufradat*) dan kaidah-kaidah dasar (*nahwu/sharaf*), namun seringkali menghadapi kendala mental dan teknis untuk mengekspresikannya dalam percakapan nyata secara spontan. Mereka membutuhkan mitra bicara yang interaktif, tidak menghakimi, dan mampu menstimulasi pembicaraan yang lebih kompleks.  
  **Sultan Hiwar** hadir sebagai solusi berbasis teknologi untuk menyediakan lingkungan berlatih yang suportif, interaktif, dan kontekstual, sekaligus memberikan umpan balik koreksi linguistik secara langsung.

---

## 🤖 Persona Chatbot: "Sultan Hiwar"

* **Nama Persona:** Sultan Hiwar (سُلْطَانُ الحِوَارِ)
* **Karakteristik & Gaya Mengajar:**
  * **Interaktif & Ramah:** Membuka sesi dengan salam Islami dan sapaan hangat untuk mencairkan suasana.
  * **Linguistik Kontekstual:** Merespons menggunakan Bahasa Arab yang fasih dan berharakat lengkap untuk melatih pendengaran dan membaca teks Arab yang benar, disertai terjemahan/bimbingan Bahasa Indonesia jika diperlukan.
  * **Pedagogis Tingkat Menengah:** Mendorong pembelajar untuk menjawab menggunakan kalimat sempurna (*jumlah mufidah*), bukan sekadar jawaban satu kata seperti *Na'am* (نَعَمْ) atau *Laa* (لَا).
  * **Sistem Koreksi Lembut (Feedback Loop):** Jika terdeteksi adanya kesalahan struktur kata (*sharaf*), tata bahasa (*nahwu*), atau diksi, Sultan Hiwar akan memberikan koreksi halus di akhir respons dengan format khusus `[Koreksi: ...]`, kemudian langsung memancing kelanjutan percakapan menggunakan pertanyaan terbuka.

---

## 🌟 Fitur-Fitur Utama Aplikasi

1. **Antarmuka Percakapan Interaktif Terminal (CLI):** Aplikasi berjalan langsung melalui baris perintah terminal dengan alur input-output yang bersih dan responsif.
2. **Riwayat Percakapan (Conversation History):** Menggunakan fitur manajemen sesi sehingga chatbot mengingat konteks obrolan sebelumnya dalam satu sesi berjalan (tidak hilang ingatan).
3. **3 Mode Pembelajaran Tematik:**
   * **Mode 1: Hiwar Tematik (Simulasi Situasi Nyata):** Melatih percakapan berbasis peran (*roleplay*), contohnya simulasi memesan makanan di restoran Arab (*fi al-mat'am*) atau situasi di bandara.
   * **Mode 2: Tanya Jawab Pendapat (Ekspresi Opini):** Mengajak pengguna berdiskusi mengenai topik tertentu, seperti *"Pentingnya teknologi dalam pembelajaran bahasa"* (*Ahammiyat ut-tiknuluujiya fi ta'allum il-lughah*), untuk melatih kemampuan berargumen.
   * **Mode 3: Tebak Kata & Deskripsi (Washf al-Hal):** Sesi interaktif di mana Sultan Hiwar memberikan skenario atau kata kunci misterius, lalu pengguna ditantang untuk mendeskripsikannya dalam Bahasa Arab tanpa menyebut kata kunci tersebut secara langsung.
4. **Auto-Feedback Log:** Format khusus `[Koreksi: ...]` yang terpisah dari narasi utama untuk mempermudah evaluasi mandiri oleh mahasiswa.
5. **Perintah Keluar Terintegrasi:** Sesi percakapan dapat diakhiri secara aman kapan saja dengan mengetikkan perintah `exit` atau `quit`.

---

## 🚀 Layanan API & Spesifikasi Teknis

* **Bahasa Pemrograman:** Python (Versi 3.8 ke atas)
* **Layanan AI API:** Google Gemini API (Menggunakan model tercepat dan paling kontekstual: `gemini-2.5-flash`)
* **Library Eksternal Utama:**
  * `google-genai` (v0.1.1) — SDK resmi Google untuk integrasi model AI Gemini.
  * `python-dotenv` (v1.0.1) — Untuk manajemen variabel lingkungan secara aman (menyembunyikan API Key).

---

## 🛠️ Panduan Instalasi & Cara Menjalankan

### 1. Kloning Repositori ke Lokal
Silakan kloning repositori GitHub ini ke komputer atau laptop Anda melalui terminal:
```bash
git clone [https://github.com/](https://github.com/)[username-github-anda]/[nama-repositori-anda].git
cd [nama-repositori-anda]