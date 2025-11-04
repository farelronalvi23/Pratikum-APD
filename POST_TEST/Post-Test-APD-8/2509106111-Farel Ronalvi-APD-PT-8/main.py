from user import registrasi, login
from barang import tampilkan_barang, tambah_barang, ubah_barang, hapus_barang
from utilitas import hitung_total_barang

def tampilkan_header():
    print("\nSelamat datang di Ronalvi Audio")
    print("-----------------------------")
    print("1. Registrasi")
    print("2. Masuk")
    print("3. Keluar")

while True:
    tampilkan_header()
    pilihan = input("Pilihan anda : ")

    if pilihan == "1":
        print("\nHalaman Registrasi")
        print("------------------")
        registrasi()

    elif pilihan == "2":
        print("\nHalaman Masuk")
        print("-------------")

        tipe = login()
        if tipe:
            while True:
                print("\nMenu Kelola Barang")
                print("---------------------")
                print("1. Tambah Barang")
                print("2. Lihat Semua Barang")
                print("3. Ubah Barang")
                print("4. Hapus Barang")
                print("5. Hitung Total Barang (Rekursif)")
                print("6. Keluar")
                print("------------------------")

                pilihan_barang = input("Pilih menu : ")

                try:
                    if pilihan_barang == '1':
                        if tipe != "admin":
                            print("Hanya admin yang boleh menambah barang!")
                            continue
                        nama = input("Nama barang : ")
                        jumlah = int(input("Jumlah barang : "))
                        harga = int(input("Harga barang : "))
                        tambah_barang(nama, jumlah, harga)

                    elif pilihan_barang == '2':
                        tampilkan_barang()

                    elif pilihan_barang == '3':
                        if tipe != "admin":
                            print("Hanya admin yang boleh mengubah barang!")
                            continue
                        nama_lama = input("Masukkan nama barang lama : ")
                        nama_baru = input("Nama baru : ")
                        jumlah_baru = int(input("Jumlah baru : "))
                        harga_baru = int(input("Harga baru : "))
                        ubah_barang(nama_lama, nama_baru, jumlah_baru, harga_baru)

                    elif pilihan_barang == '4':
                        if tipe != "admin":
                            print("Hanya admin yang boleh menghapus barang!")
                            continue
                        hapus_barang()

                    elif pilihan_barang == '5':
                        jumlah_seluruh = hitung_total_barang()
                        print(f"Total semua jumlah barang adalah: {jumlah_seluruh}")

                    elif pilihan_barang == '6':
                        break
                    else:
                        print("Pilihan menu tidak valid.")
                except ValueError:
                    print("Input tidak sesuai, masukkan angka dengan benar!")

    elif pilihan == "3":
        print("Program berhenti!")
        break
    else:
        print("Pilihan tidak valid!")
