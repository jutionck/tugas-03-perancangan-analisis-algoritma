# Algoritma yang dapat dilakukan adalah
# 1. Minta input panjang sisi A, sisi B, dan sisi C dari pengguna.
# 2. Jika A = B = C, cetak "SAMA SISI".
# 3. Jika A = B atau B = C atau A = C, cetak "SAMA KAKI".
# 4. Jika tidak, cetak "SEMBARANG".
# 5. Selesai.

# Program
def triangleCheck(side1, side2, side3):
    if side1 == side2 == side3:
        return "SAMA SISI"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "SAMA KAKI"
    else:
        return "SEMBARANG"

# Minta pengguna memasukkan panjang sisi segitiga
side1 = float(input("Masukkan panjang sisi pertama: "))
side2 = float(input("Masukkan panjang sisi kedua: "))
side3 = float(input("Masukkan panjang sisi ketiga: "))

output = triangleCheck(side1, side2, side3)

# Cetak jenis segitiga
print("Jenis segitiga:", output)
