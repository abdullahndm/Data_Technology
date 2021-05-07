# Membuat fungsi berparameter
def kali(x: float, y: float):
    hasil = x * y
    return hasil


# Pencabangan
def tentukan_nilai_huruf(nilai_angka: float):
    # 50 ke bawah: C
    if nilai_angka <= 50:
        nilai_huruf = 'C'
    elif nilai_angka > 50 and nilai_angka < 80:  # 51 s.d. 79 dapat B, elif --> else if
        nilai_huruf = 'B'
    else:
        nilai_huruf = 'A'
    return nilai_huruf


# Perulangan - WHILE
def ulangi_kata(kata: str, jumlah: int):
    hasil = ''
    x = 0
    while x < jumlah:
        hasil = (hasil + ', ' + kata)
        x = (x + 1)
    return hasil


# Perulangan dengan menggunakan FOR ... IN
def sebutkan_nama_hari():
    seminggu = [
        'Senin',
        'Selasa',
        'Rabu',
        'Kamis',
        'Jumat',
        'Sabtu',
        'Minggu'
    ]

    for hari in seminggu:
        print(hari)

def main():
    # Membuat variabel, memberikan nilai
    x = 20  # 0x1054deb90
    alamat_x = hex(id(x))
    print(x)
    print(alamat_x)
    # Mengubah nilai variabel
    x = x + 1
    print(x)
    print(hex(id(x)))
    x = "Apa kabar, X?"  # Memberikan nilai yang lain
    print(x)  # 0x1054deb90
    print(hex(id(x)))

    # Memanggil fungsi
    b1 = 9.5
    b2 = 9.75
    hasil_perkalian = kali(b1, b2)
    print(hasil_perkalian)

    # Panggil fungsi pencabangan
    nilai_angka = 85
    nilai_huruf = tentukan_nilai_huruf(nilai_angka)
    print("Nilai huruf: " + nilai_huruf)  # Menggabungkan string bisa dengan +

    # Pencabangan - WHILE
    kata_diulang = ulangi_kata('Halo', 7)
    print(kata_diulang)

    # Pencabangan - FOR ... IN
    sebutkan_nama_hari()

    # Input <-- Semua hasil dari fungsi input, berupa STR
    nama = input("Masukkan nama: ")
    tahun_lahir = input("Tahun lahir Anda: ")
    # FORMAT(), dengan placeholder
    # Halo nama, anda lahir pada YYYY.
    salam = "Halo {}, anda lahir pada {}".format(nama, tahun_lahir)
    print(salam)
    # Konversi str ke int
    tahun_lahir = int(tahun_lahir) # Dynamic Typing
    umur = 2021 - tahun_lahir
    print(umur)


main()
