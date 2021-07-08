import csv
import os

csv_filename = 'Data/Buku.csv'
csv_filename1 = 'Data/Peminjam.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():

    clear_screen()

    print("===========================================")
    print("=== Selamat Datang di Perpustakaan D3TI ===")
    print("================== Menu ===================")
    print("[1] Lihat Daftar Buku")
    print("[2] Tambah Buku")
    print("[3] Hapus Buku")
    print("[4] Pinjam Buku")
    print("[5] Kembalikan Buku")
    print("[0] Exit")
    print("===========================================")
    selected_menu = input("Pilih Menu> ")

    if(selected_menu == "1"):
        show_buku()
    elif(selected_menu == "2"):
        tambah_buku()
    elif(selected_menu == "3"):
        delete_buku()
    elif(selected_menu == "4"):
        tambah_peminjam()
    elif(selected_menu == "5"):
        delete_peminjam()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Menu Salah. Masukkan Angka!")
        back_to_menu()

def back_to_menu():
    print("")
    input("Tekan Enter Untuk Kembali...")
    show_menu()

def show_buku():
    clear_screen()
    Buku = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Buku.append(row)

    row_count = sum(1 for row in Buku)

    print("-" * 115)
    print("\t\t\t\t\t\t Daftar Buku")
    print("-" * 115)
    print("Kode \t Judul \t\t\t\t\t Penulis \t\t\t\t Penerbit")
    print("-" * 115)

    for data in Buku:
        print(
            f"{data['Kode']} \t {data['JUDUL']} \t\t\t\t {data['PENULIS']} \t\t\t\t {data['PENERBIT']}")
    print("-" * 115)
    print("Total Data: ", row_count)
    print("-" * 115)

    back_to_menu()

def tambah_buku():
    clear_screen()
    Buku = []
    with open(csv_filename, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Buku.append(row)
        print("-" * 115)
        print("Kode \t Judul \t\t\t\t\t Penulis \t\t\t\t Penerbit")
        print("-" * 115)

    for data in Buku:
        print(
            f"{data['Kode']} \t {data['JUDUL']} \t\t\t\t {data['PENULIS']} \t\t\t\t {data['PENERBIT']}")

    with open(csv_filename, mode='a', newline='') as csv_file:
        fieldnames = ['kode', 'JUDUL', 'PENULIS', 'PENERBIT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("-" * 115)
        print("Masukkan Data Buku Untuk Ditambah! [Kode 0 Untuk Batal]")
        kode = input("Kode: ")
        if (kode == "0"):
            show_menu()
        judul = input("Judul: ")
        penulis = input("Penulis: ")
        penerbit = input("Penerbit: ")

        print("===============================")

        writer.writerow({'kode': kode, 'JUDUL': judul, 'PENULIS': penulis, 'PENERBIT': penerbit})

    back_to_menu()


def tambah_peminjam():
    clear_screen()
    Pinjam = []
    with open(csv_filename1, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Pinjam.append(row)
        print("-" * 120)
        print(
            "Kode Peminjaman    Nama Peminjam \t\t Telepon Peminjam \t\t Buku Yang Dipinjam")
        print("-" * 120)

    for data in Pinjam:
        print(
            f"{data['Kode']} \t\t   {data['NAMA']} \t\t\t {data['TELEPON']} \t\t\t {data['PINJAM']}")

    with open(csv_filename1, mode='a', newline='') as csv_file:
        fieldnames = ['kode', 'NAMA', 'TELEPON', 'PINJAM']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("-" * 120)
        print("Masukkan Data Peminjam! [Kode 0 Untuk Batal]")
        kode = input("Kode Peminjaman: ")
        if (kode == "0"):
            show_menu()
        nama = input("Nama Peminjam: ")
        telepon = input("Telepon Peminjam: ")
        pinjam = input("Buku Yang Dipinjam: ")

        print("===============================")

        writer.writerow({'kode': kode, 'NAMA': nama, 'TELEPON': telepon, 'PINJAM': pinjam})
    back_to_menu()

def delete_buku():
    clear_screen()
    Buku = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Buku.append(row)

    print("-" * 115)
    print("Kode \t Judul \t\t\t\t\t Penulis \t\t\t\t Penerbit")
    print("-" * 115)

    for data in Buku:
        print(
            f"{data['Kode']} \t {data['JUDUL']} \t\t\t\t {data['PENULIS']} \t\t\t\t {data['PENERBIT']}")
    print("-" * 115)

    kode = input("Hapus Buku dengan KODE [0 Untuk Batal]: ")
    if (kode == "0"):
        show_menu()

    indeks = 0
    for data in Buku:
        if (data['Kode'] == kode):
            Buku.remove(Buku[indeks])
        indeks = indeks + 1

    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'JUDUL', 'PENULIS', 'PENERBIT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Buku:
            writer.writerow({'Kode': new_data['Kode'], 'JUDUL': new_data['JUDUL'], 'PENULIS': new_data['PENULIS'], 'PENERBIT': new_data['PENERBIT']})

    print("Data Buku Berhasil Dihapus!")
    back_to_menu()


def delete_peminjam():
    clear_screen()
    Pinjam = []

    with open(csv_filename1, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Pinjam.append(row)

    print("-" * 120)
    print("Kode Peminjaman    Nama Peminjam \t\t Telepon Peminjam \t\t Buku Yang Dipinjam")
    print("-" * 120)

    for data in Pinjam:
        print(
            f"{data['Kode']} \t\t   {data['NAMA']} \t\t\t {data['TELEPON']} \t\t\t {data['PINJAM']}")
    print("-" * 120)

    kode = input("Kembalikan Buku dengan KODE PEMINJAMAN [0 Untuk Batal]: ")
    if (kode == "0"):
        show_menu()

    indeks = 0
    for data in Pinjam:
        if (data['Kode'] == kode):
            Pinjam.remove(Pinjam[indeks])
        indeks = indeks + 1

    with open(csv_filename1, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'TELEPON', 'PINJAM']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Pinjam:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON'], 'PINJAM': new_data['PINJAM']})

    print("Buku Telah Dikembalikan, Data Berhasil Dihapus!")
    back_to_menu()


if __name__ == "__main__":
    while True:
        show_menu()
