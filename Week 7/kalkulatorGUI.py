import tkinter as tk
from doctest import master


class KalkulatorGUI:

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.geometry('360x200')
        self.__window.title('Kalkulator GUI - Abdullah')
        # Gambar widget-widget di Window
        self.__init_widgets()

    def __init_widgets(self):
        print('Membuat widget-widget..')

        # 1. Buat label-label dengan frame
        self.__frame_kiri = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__frame_kanan = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__lbl_b1 = tk.Label(master=self.__frame_kiri, text='Bilangan-1: ')
        self.__lbl_b2 = tk.Label(master=self.__frame_kiri, text='Bilangan-2: ')
        self.__lbl_hasil = tk.Label(master=self.__frame_kiri, text='Hasil: ')
        self.__lbl_nama = tk.Label(master=self.__frame_kanan, text='by Abdullah ')
        self.__lbl_b1.pack(pady=3)
        self.__lbl_b2.pack(pady=3)
        self.__lbl_hasil.pack(pady=3.5)
        self.__lbl_nama.pack(pady=3.5)
        self.__frame_kiri.grid(row=0, column=0, sticky='nw')
        self.__frame_kanan.grid(row=2, column=0, sticky='nw')

        # 2. Buat textbox-nya
        self.__frame_kanan = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__ent_b1 = tk.Entry(master=self.__frame_kanan, width=25)
        self.__ent_b2 = tk.Entry(master=self.__frame_kanan, width=25)
        self.__ent_hasil = tk.Entry(master=self.__frame_kanan, width=25)
        self.__ent_nama = tk.Entry(master=self.__frame_kiri, width=25)
        self.__ent_b1.pack(pady=3)
        self.__ent_b2.pack(pady=3)
        self.__ent_hasil.pack(pady=3.5)
        self.__frame_kanan.grid(row=0, column=1, sticky='ne')

        # 3. Buat button hitung
        self.__frame_bawah = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__btn_reset = tk.Button(master=self.__frame_bawah, text='Reset')
        self.__btn_tambah = tk.Button(master=self.__frame_bawah, text=' + ')
        self.__btn_kurang = tk.Button(master=self.__frame_bawah, text=' - ')
        self.__btn_kali = tk.Button(master=self.__frame_bawah, text=' * ')
        self.__btn_bagi = tk.Button(master=self.__frame_bawah, text=' / ')
        self.__btn_reset.pack(side=tk.LEFT)
        self.__btn_tambah.pack(side=tk.LEFT)
        self.__btn_kurang.pack(side=tk.LEFT)
        self.__btn_kali.pack(side=tk.LEFT)
        self.__btn_bagi.pack(side=tk.LEFT)
        self.__frame_bawah.grid(row=1, column=1, sticky='sw')

        # 4. Bind action ke button
        self.__btn_reset.bind('<Button-1>', self.__on_btn_reset_left_click)
        self.__btn_tambah.bind('<Button-1>', self.__on_btn_tambah_left_click)
        self.__btn_kurang.bind('<Button-1>', self.__on_btn_kurang_left_click)
        self.__btn_kali.bind('<Button-1>', self.__on_btn_kali_left_click)
        self.__btn_bagi.bind('<Button-1>', self.__on_btn_bagi_left_click)

    # 5. Action untuk button reset
    def __on_btn_reset_left_click(self, event: tk.Event):
        print('btn_reset click..')
        self.__ent_b1.delete(0, tk.END)
        self.__ent_b2.delete(0, tk.END)
        self.__ent_hasil.delete(0, tk.END)

    # 6. Action untuk button hitung tambah, kurang, kali, bagi
    def __on_btn_tambah_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) + float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))

    def __on_btn_kurang_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) - float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))

    def __on_btn_kali_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) * float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))

    def __on_btn_bagi_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) / float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))

    def show(self):
        self.__window.mainloop()
