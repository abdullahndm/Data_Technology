import pandas as pd


class LatihanPandas:

    def __init__(self):
        self.data = None

    def tampilkan_pilihan(self):
        print('Latihan Pandas')
        print('--------------')
        print('Menu:')
        print('(1) Load dataset')
        print('(2) Tampilkan 5 baris teratas dan terakhir')
        print('(3) Tampilkan data jurusan Teknik Informatika')
        print('(4) Tampilkan kolom nama dan prodi')
        print('(0) Keluar')
        pilihan = input('Pilihan Anda? ')
        if pilihan == '1':
            self.load_dataset()
            return True
        elif pilihan == '2':
            self.tampilkan_5_baris_awal_akhir()
            return True
        elif pilihan == '3':
            self.tampilkan_data_jurusan()
            return True
        elif pilihan == '4':
            self.tampilkan_nama_dan_prodi()
            return True
        else:
            return False

    def load_dataset(self):
        print('Memuat dataset..')
        # Hasil import sebagai DataFrame
        # https://stackoverflow.com/questions/18039057/python-pandas-error-tokenizing-data
        # https://www.shanelynn.ie/pandas-csv-error-error-tokenizing-data-c-error-eof-inside-string-starting-at-line/
        self.data = pd.read_csv(
            'files/mahasiswa.csv',
            sep=',',                      # Separator
            error_bad_lines=False,        # Skip baris yang error
            engine='python'               # Mengganti Parser engine dari C ke Python
        )
        # Set kolom 'id' sebagai index
        self.data.set_index('id')
        # Cetak di console
        print(self.data.to_string())

    def tampilkan_nama_dan_prodi(self):
        print('Memilih kolom tertentu..')
        # Mengambil berdasarkan nama kolom
        nama = self.data['nama']
        # Bisa juga dengan cara seperti ini
        prodi = self.data.prodi
        # Menggabungkan 2 DataFrame
        # # A. Digabungkan barisnya (Ditumpuk)
        # gabung_baris = pd.concat([nama, prodi], axis=0)
        # print(gabung_baris.to_string())
        # B. Digabungkan kolomnya (Digandeng)
        gabung_kolom = pd.concat([nama, prodi], axis=1)
        print(gabung_kolom.to_string())

    def tampilkan_5_baris_awal_akhir(self):
        print('Menyeleksi beberapa baris di awal dan akhir..')
        # Mengambil N-baris teratas
        awal5 = self.data.head(5)
        print(awal5.to_string())
        # # Mengambil N-baris terakhir
        # akhir5 = self.data.tail(5)
        # print(akhir5.to_string())

    def tampilkan_data_jurusan(self):
        print('Seleksi baris dengan WHERE')
        # Membuat filter untuk WHERE
        filter = self.data['jurusan'] == 'Teknologi Informasi'
        # Seleksi data
        data_si = self.data.where(filter)
        print(data_si)

