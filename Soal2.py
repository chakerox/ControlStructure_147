a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    print("Angka terbesar:", a)
elif b >= a and b >= c:
    print("Angka terbesar:", b)
else:
    print("Angka terbesar:", c)