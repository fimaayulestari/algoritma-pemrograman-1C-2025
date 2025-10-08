umur = 20

if umur >= 18:
    print("Anda sudah dewasa")


umur = 15

if umur >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda belum dewasa")


nilai = 75

if nilai >= 85:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("D")


umur = 20
status = "pelajar"

if umur >= 18:
    if status == "pelajar":
        print("Anda pelajar dewasa")
    else:
        print("Anda dewasa")
else:
    print("Anda belum dewasa")


umur = 18
pesan = "Dewasa" if umur >= 18 else "Belum dewasa"
print(pesan)