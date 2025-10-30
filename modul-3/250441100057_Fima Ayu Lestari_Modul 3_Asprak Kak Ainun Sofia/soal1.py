# Tugas no 1

# batas = int(input("masukkan batas angka akhir :"))

# print("Bilangan prima dari 1 sampai", batas, ":")

# for angka in range(2, batas + 1):
#     prima = True
#     for pembagi in range(2, angka):
#         if angka % pembagi == 0:
#             prima = False
#             break
#     if prima:
#         print(angka)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# for i in range(1, 4):        # Perulangan luar
#     for j in range(1, 4):    # Perulangan dalam
#         print(j)

# data = [1, 2, 3, 4, 5]

# for i in data:
#     for j in data:
#         if i != j:
#             print(i, j)

a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b

# Program pola piramida angka sederhana

baris = int(input("Masukkan jumlah baris: "))

for i in range(1, baris + 1):
    # Cetak spasi biar bentuknya seperti piramida
    print(" " * (baris - i), end="")
    
    # Cetak angka naik di setiap baris
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Pindah ke baris baru
    print()
