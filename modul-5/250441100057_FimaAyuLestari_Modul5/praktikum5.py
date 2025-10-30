 
# no 1

# def salam():
#     print("Selamat pagi!")
# salam()

# no 6
def hitung_tagihan(kwh):
    tarif = 1500
    total = kwh * tarif
    return total

def kategori(kwh):
    if kwh >= 500:
        return "Penggunaan Tinggi"
    else:
        return "Penggunaan Normal"

pemakaian = float(input("Masukkan pemakaian listrik (kWh): "))
tagihan = hitung_tagihan(pemakaian)
status = kategori(pemakaian)

print("Total tagihan listrik: Rp", tagihan)
print("Kategori:", status)



# def sapa():
#     print("Hallo Dunia!")

# # sapa()

# def sapa2():
#     sapa()
#     print("Hallo saya menyapa dua kali")

# sapa2()

# def tambah (a, b):
#     c = a + b
#     print("hasil penjumlahan :", c)
#     return c

# tambah(3, 4)

# lamabda cuma satu baris dengan beberapa parameter dan diikuti tugasnya

# tambah = lambda x, y, z: x + y + z
# print(tambah(10, 2, 5)) 

# print((lambda k:k*3)(3)) # k sebagai parameter bisa terserah yang penting bukan angaka
# print((lambda k:k*3)(6))

# fungsi rekrusif

def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)
    
print(faktorial(3))
# 3 * faktorial(2)
# 2 * faktorial(1)
# 1

# soal ni 6 tp
def hitung(kwh):
    tarif_dasar = 1500
    total = kwh * tarif_dasar
    return total

def kategori(kwh):
    if kwh >= 500:
        return("prnggunaan tinggi")
    else:
        return("penggunaan normal")
    
print("program menghitung listrik")
kwh = int(input("masukkan jumlah pemakaian listrik (kwh): "))
print("jumlah pemakaian:", hitung(kwh))
print("kategori pemakaian:", kategori(kwh))
print("terimakasih")