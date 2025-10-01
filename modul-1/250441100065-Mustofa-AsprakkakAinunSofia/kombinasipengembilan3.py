# Program menghitung kombinasi pengambilan bola menggunakan operator aritmatika

# Data jumlah bola
bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru  # 8 + 6 = 14
r = 3  # jumlah bola yang diambil

# Hitung pembilang dengan operator aritmatika (* dan -)
pembilang = total_bola * (total_bola - 1) * (total_bola - 2)

# Hitung penyebut dengan operator aritmatika (* dan -)
penyebut = r * (r - 1) * (r - 2)

# Hitung kombinasi dengan operator pembagian (/)
kombinasi = pembilang / penyebut

# Tampilkan hasil
print("Total bola:", total_bola)
print("Jumlah bola yang diambil:", r)
print("Jumlah kombinasi yang mungkin:", kombinasi)
