def hitung (a1, a2, opsi):
    if opsi == "*":
        hasil = a1 * a2
        print("Hasil perkalian dari {} dan {} adalah {}".format(a1,a2,hasil))
    elif opsi == "+":
        hasil = a1 + a2
        print("Hasil penjumlahan dari {} dan {} adalah {}".format(a1, a2, hasil))
    elif opsi == "-":
        hasil = a1 - a2
        print("Hasil pengurangan dari {} dan {} adalah {}".format(a1, a2, hasil))
    elif opsi == "/":
        hasil = a1 / a2
        print("Hasil pembagian dari {} dan {} adalah {}".format(a1, a2, hasil))
    else:
        print("operator yang anda inputkan salah, masukan operator berikut +, -, *, / ")

def ask (a,b,c):
    if c == a:
        main()
    elif c == b:
        print("Baiklah, Selamat Belajar !")
        quit()


def main():
    angka1 = input("Masukkan bilangan-1 : ")
    angka2 = input("Masukkan bilangan-2 : ")
    opsi = input("Masukkan operator : ")
    a1 = int(angka1)
    a2 = int(angka2)
    a = opsi
    hitung(a1,a2,a)
    tanya = input("Hitung kembali ? (Y/N) : ")
    a = "y" or "Y"
    b = "n" or "N"
    c = tanya
    ask(a,b,c)

main()