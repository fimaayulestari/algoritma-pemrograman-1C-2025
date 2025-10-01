#Modul 1 Praktikum
#Soal 1
harga_buku_tulis = 5000
harga_pensil = 4500
pajak = 0.10
j_buku_tulis = 3
j_pensil = 2

j_buku_tulis = harga_buku_tulis * j_buku_tulis
j_pensil = harga_pensil * j_pensil
total_biaya = j_buku_tulis + j_pensil
pajak = total_biaya * pajak
setelah_pajak = total_biaya + pajak

print(f"total biaya: Rp.{total_biaya}")
print(f"pajak 10%: Rp.{pajak}")
print(f"total biaya : Rp.{setelah_pajak}")

#Soal 2
panjang = float(input("Masukkan panjang : "))   #10
lebar = float(input("Masukkan lebar : "))    #6  
tinggi = float(input("Masukkan tinggi : "))  #4

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print(f"Volume Balok : {volume}cm³")
print(f"Luas Permukaan Balok : {luas_permukaan}cm")

#Soal 3
bola_merah = 8
bola_biru = 6
tb = 14
a = 3

numerator = tb * (tb-1) * (tb-2)
denominator = a * (a-1) * (a-2)
kombinasi = numerator // denominator

print(f"jumlah bola merah: {bola_merah}")
print(f"jumlah bola biru: {bola_biru}")
print(f"total bola: {tb}")
print(f"jumlah bola yang diambil: {a}")
print(f"dumerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")