
print("PROGRAM ANALISIS PERSAMAAN KUADRAT")

a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
c = float(input("Masukkan nilai c : "))

if a == 0:
    print("Bukan persamaan kuadrat")
else:
    diskriminan = (b ** 2) - (4 * a * c)

    print("\nDiskriminan =", diskriminan)

    if diskriminan > 0:
        print("Memiliki 2 akar real berbeda")
    elif diskriminan == 0:
        print("Memiliki 1 akar real kembar")
    else:
        print("Tidak memiliki akar real")
