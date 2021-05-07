def tambah(x: int, y: int):
    return x + y


def kurang(x: int, y: int):
    return x - y


def prompt():
    i1 = input("Masukkan bilangan-1: ")
    i2 = input("Masukkan bilangan-2: ")
    b1 = int(i1)
    b2 = int(i2)
    operator = input("Masukkan operator: ")
    if operator == '+':
        hasil = tambah(b1, b2)
        nama_operator = 'Penjumlahan'
        print('Hasil {} antara {} dan {} adalah: {}'.format(nama_operator, b1, b2, hasil))
    elif operator == '-':
        hasil = kurang(b1, b2)
        nama_operator = 'Pengurangan'
        print('Hasil {} antara {} dan {} adalah: {}'.format(nama_operator, b1, b2, hasil))
    else:
        hasil = "Operator tidak valid!"
        print(hasil)
    lagi = input("Lagi? (Y/T): ")
    return lagi


def loop():
    lagi = 'Y'
    while lagi == 'Y' or lagi == 'y':
        lagi = prompt()


loop()