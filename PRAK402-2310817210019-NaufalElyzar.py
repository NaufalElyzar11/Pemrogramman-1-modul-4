def genap(angka):
    for i in range(angka, 0, -1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def ganjil(angka):
    for i in range(1, angka + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def main():
    angka = int(input())
    ganjil(angka)
    genap(angka)

if __name__ == "__main__":
    main()
