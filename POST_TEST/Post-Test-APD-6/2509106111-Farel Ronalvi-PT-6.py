username = []
password = []

barang = {
    "Speaker Yamaha DBR 15": {"jumlah": 10, "harga": 5000000},
    "Midas M32": {"jumlah": 5, "harga": 3000000},
    "Shure SM 58": {"jumlah": 20, "harga": 750000},
    "Kabel xlr 5m": {"jumlah": 50, "harga": 150000},
    "Stand Speaker": {"jumlah": 15, "harga": 350000}
}

while True:
    print("\nSelamat datang di Ronalvi Audio")
    print("-----------------------------")
    print("1. Registrasi")
    print("2. Masuk")
    print("3. Keluar")

    pilihan = input("Pilihan anda : ")

    if pilihan == "1":
        print("\nHalaman Registrasi")
        print("------------------")

        while True:
            usernameBaru = input("Masukkan username anda : ")
            if usernameBaru in username:
                print("Username telah digunakan, pilih username lain!")
            else:
                username.append(usernameBaru)
                passwordBaru = input("Masukkan password anda : ")
                password.append(passwordBaru)
                print("Registrasi telah berhasil!")
                break

    elif pilihan == "2":
        print("\nHalaman Masuk")
        print("-------------")

        if not username:
            print("Belum ada akun yang terdaftar!")
            continue

        loginUsername = input("Masukkan username anda : ")
        loginPassword = input("Masukkan password anda : ")

        if loginUsername in username:
            user_index = username.index(loginUsername)

            if password[user_index] == loginPassword:
                print("\nLogin berhasil!")

                while True:
                    print("\nMenu Kelola Barang")
                    print("---------------------")
                    print("1. Tambah Barang")
                    print("2. Lihat Semua Barang")
                    print("3. Ubah Barang")
                    print("4. Hapus Barang")
                    print("5. Keluar")
                    print("------------------------")

                    pilihan_barang = input("Pilih menu : ")

                    if pilihan_barang == '1':
                        print("\nTambah Barang Baru")
                        print("----------------------")
                        nama = input("Nama barang : ")
                        jumlah = int(input("Jumlah barang : "))
                        harga = int(input("Harga barang : "))

                        barang[nama] = {"jumlah": jumlah, "harga": harga}
                        print(f"Barang '{nama}' berhasil ditambahkan.")

                    elif pilihan_barang == '2':
                        print("\nDaftar Barang")
                        print("----------------")
                        if not barang:
                            print("Belum ada barang di daftar.")
                        else:
                            nomor = 1
                            for nama in barang:
                                info = barang[nama]
                                print(f"{nomor}. Nama  : {nama}")
                                print(f"   Jumlah: {info['jumlah']}")
                                print(f"   Harga : Rp.{info['harga']}")
                                print("   -----------")
                                nomor += 1

                    elif pilihan_barang == '3':
                        print("\nUbah Barang")
                        print("--------------")
                        if not barang:
                            print("Tidak ada barang untuk diubah.")
                        else:
                            daftar_nama = list(barang.keys())
                            nomor = 1
                            for nama in daftar_nama:
                                print(f"{nomor}. {nama}")
                                nomor += 1

                            nomor_pilih = int(input("Pilih nomor barang yang mau diubah: "))
                            if 1 <= nomor_pilih <= len(daftar_nama):
                                nama_lama = daftar_nama[nomor_pilih - 1]
                                nama_baru = input(f"Masukkan nama baru untuk '{nama_lama}' : ")
                                jumlah_baru = int(input("Masukkan jumlah baru : "))
                                harga_baru = int(input("Masukkan harga baru : "))

                                barang.pop(nama_lama)
                                barang[nama_baru] = {"jumlah": jumlah_baru, "harga": harga_baru}
                                print("Barang berhasil diubah.")
                            else:
                                print("Nomor barang tidak valid.")

                    elif pilihan_barang == '4':
                        print("\nHapus Barang")
                        print("----------------")
                        if not barang:
                            print("Tidak ada barang untuk dihapus.")
                        else:
                            daftar_nama = list(barang.keys())
                            nomor = 1
                            for nama in daftar_nama:
                                print(f"{nomor}. {nama}")
                                nomor += 1

                            nomor_hapus = int(input("Pilih nomor barang yang mau dihapus: "))
                            if 1 <= nomor_hapus <= len(daftar_nama):
                                nama_hapus = daftar_nama[nomor_hapus - 1]
                                barang.pop(nama_hapus)
                                print(f"Barang '{nama_hapus}' berhasil dihapus.")
                            else:
                                print("Nomor barang tidak valid.")

                    elif pilihan_barang == '5':
                        break

                    else:
                        print("Pilihan menu barang tidak ada!")

            else:
                print("Password salah.")
        else:
            print("Username tidak ditemukan.")

    elif pilihan == "3":
        print("Program berhenti!") 
        break

    else:
        print("Pilihan tidak valid!")
