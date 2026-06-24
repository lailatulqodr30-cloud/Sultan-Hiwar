import os
from google import genai # Menggunakan Google GenAI SDK terbaru
from dotenv import load_dotenv

# 1. Load API Key dari file .env (Sesuai Ketentuan Keamanan)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY tidak ditemukan di file .env!")
    exit()

# Inisialisasi Client Gemini
client = genai.Client(api_key=API_KEY)

# 2. Definisikan System Prompt Persona
SYSTEM_PROMPT = """
Kamu adalah 'Sultan Hiwar', tutor AI ramah untuk Maharah Kalam tingkat menengah.
Gunakan Bahasa Arab berharakat dan berikan koreksi lembut jika pengguna salah dalam menyusun kalimat.
"""

def main():
    print("====================================================")
    print("🎉 Selamat Datang di Chatbot Pembelajaran Bahasa Arab 🎉")
    print("====================================================")
    
    # 3. Fitur Pilihan Mode Pembelajaran
    print("\nPilih Mode Pembelajaran Sultan Hiwar:")
    print("1. Hiwar Tematik (Simulasi Situasi)")
    print("2. Tanya Jawab Pendapat (Ekspresi Opini)")
    print("3. Tebak Kata & Deskripsi (Kreativitas Kalam)")
    
    pilihan = input("\nMasukkan nomor mode (1/2/3): ")
    
    # Menentukan konteks tambahan berdasarkan mode yang dipilih
    mode_context = ""
    if pilihan == "1":
        mode_context = "Mode aktif: Hiwar Tematik di Restoran."
    elif pilihan == "2":
        mode_context = "Mode aktif: Diskusi Opini tentang Teknologi."
    else:
        mode_context = "Mode aktif: Tebak Kata/Deskripsi Sederhana."

    # 4. Memulai Sesi Chat dengan History
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": SYSTEM_PROMPT + "\n" + mode_context
        }
    )
    
    # Pesan Pembuka Manual / Trigger Pertama dari AI
    print("\n[Sultan Hiwar]: Ahlan wa sahlan! Ana Sultan Hiwar. Marhaban bika fi mustawa al-mutawassit. Let's start!")
    
    # Loop Percakapan (Interactive Terminal)
    while True:
        user_input = input("\nKamu: ")
        
        # Perintah keluar aplikasi
        if user_input.lower() in ['exit', 'quit']:
            print("\n[Sultan Hiwar]: Ilalliqo'! Ma'as salamah. Semangat terus belajar kalamnya!")
            break
            
        if not user_input.strip():
            continue
            
        # Mengirim pesan ke AI (Riwayat otomatis tersimpan dalam objek 'chat')
        response = chat.send_message(user_input)
        print(f"\n[Sultan Hiwar]: {response.text}")

if __name__ == "__main__":
    main()