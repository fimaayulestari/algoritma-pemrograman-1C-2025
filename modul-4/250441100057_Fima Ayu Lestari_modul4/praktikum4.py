# for i in range(1, 5):
#     print(i)

# count = 0
# for i in range(2, 5):
#     for j in range(i):
#         count += j

# print(count)

# for i in range(3):
#     for j in range(2):
#         print(i+j, end=" ")

# total = 0

# for i in range(1, 4):
#     for j in range(1, i + 1):
#         total += i + j
#         print(total)

# # 2 3 4 4 5 6


baris = int(input("masukkan jumlah baris: "))
for i in range(1, baris + 1):
    print(" " * (baris - i), end = "")
    for j in range(1, i + 1):
        print(j, end = " ")
    print()