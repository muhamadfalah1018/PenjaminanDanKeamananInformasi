from autokey import enkripsi_autokey, dekripsi_autokey
from transposition import enkripsi_transposisi, dekripsi_transposisi

print("=== SUPER ENKRIPSI (AUTOKEY + TRANSPOSISI) ===")

pesan = input("Masukkan pesan: ")
kunci_autokey = input("Masukkan kunci Autokey: ")
kunci_transposisi = input("Masukkan kunci Transposisi: ")

# ENKRIPSI
tahap1 = enkripsi_autokey(pesan, kunci_autokey)
cipher = enkripsi_transposisi(tahap1, kunci_transposisi)

print("\nHasil Enkripsi:", cipher)

# DEKRIPSI
step1 = dekripsi_transposisi(cipher, kunci_transposisi)
plain = dekripsi_autokey(step1, kunci_autokey)

print("Hasil Dekripsi:", plain)