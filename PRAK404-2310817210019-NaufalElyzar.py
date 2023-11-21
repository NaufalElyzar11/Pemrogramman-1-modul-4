while True:
    print("Pilih Program\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Exit")
    a = int(input("Masukkan Pilihan : "))

    if 1 <= a <= 4:
        n1 = float(input("\nMasukkan Nilai Pertama : "))
        n2 = float(input("Masukkan Nilai Kedua : "))

        if a == 1:
            h1 = n1 + n2
            print(f"\nHasil Penjumlahan antara {n1:.2f} dan {n2:.2f} adalah {h1:.2f}\n")
        elif a == 2:
            h2 = n1 - n2
            print(f"\nHasil Pengurangan antara {n1:.2f} dan {n2:.2f} adalah {h2:.2f}\n")
        elif a == 3:
            h3 = n1 * n2
            print(f"\nHasil Perkalian antara {n1:.2f} dan {n2:.2f} adalah {h3:.2f}\n")
        elif a == 4:
            if n2 != 0:
                h4 = n1 / n2
                print(f"\nHasil Pembagian antara {n1:.2f} dan {n2:.2f} adalah {h4:.2f}\n")
            else:
                print("Error! Pembagian dengan nol tidak diperbolehkan.\n")
        else:
            break
    elif a == 5:
        print("\nTerimakasih, telah menggunakan kalkulator Naufal Elyzar\n\n")
        break
    else:
        print("\nInput anda salah, silahkan coba lagi\n\n")
