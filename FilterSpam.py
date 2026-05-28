# ================================================
#           FILTER SPAM EMAIL SEDERHANA
# ================================================

# Kumpulan kata-kata yang sering muncul di email spam
spam_words = {"promo", "diskon", "hadiah", "gratis", "menang","bonus"}

# ===========================
# DATA EMAIL YANG AKAN DICEK
# ===========================

emails = [
    {"subject": "SELAMAT! Anda Memenangkan Hadiah Gratis!",
     "body": "Klik disini untuk klaim promo dan diskon spesial hari ini"},
    {"subject": "Meeting besok jam 10 pagi",
     "body": "Halo, tolong konfirmasi kehadiran rapat besok ya"},
    {"subject": "Penawaran Terbatas Untuk Anda!",
     "body": "Dapatkan bonus cashback dan hadiah menarik sekarang"}
    ]

# ================
# FUNGSI CEK SPAM
# ================

def cek_spam(subject, body):
    # Gabungkan subject dan body lalu ubah ke huruf kecil
    full_text = (subject + " " + body).lower()
    
    # Pecah jadi kata-kata lalu bandingkan dengan spam_words
    kata_ditemukan = spam_words & set(full_text.split())
    
    # Hitung berapa banyak kata spam yang ditemukan
    jumlah_kata = len(kata_ditemukan)
    
    if jumlah_kata == 0:
        status = "AMAN"
        keterangan = "Email ini bukan spam"
    elif jumlah_kata <= 2:
        status = "MENCURIGAKAN"
        keterangan = f"Ditemukan kata: {kata_ditemukan}"
    else:
        status = "SPAM"
        keterangan = f"Ditemukan kata: {kata_ditemukan}"
    
    return status, keterangan

# ===============================
# JALANKAN CEK UNTUK SEMUA EMAIL
# ===============================
print("=" * 50)
print("       HASIL PENGECEKAN EMAIL SPAM")
print("=" * 50)

for i, email in enumerate(emails, 1):
    status, keterangan = cek_spam(email["subject"], email["body"])
    
    print(f"\n Email {i}")
    print(f"   Subject : {email['subject']}")
    print(f"   Status  : {status}")
    print(f"   Info    : {keterangan}")
    print("-" * 50)

print("\n Pengecekan selesai!")
