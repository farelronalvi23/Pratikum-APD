username = []
password = []
tipe_akun = []  
barang = {
    "Speaker Yamaha DBR 15": {"jumlah": 10, "harga": 5000000},
    "Midas M32": {"jumlah": 5, "harga": 3000000},
    "Shure SM 58": {"jumlah": 20, "harga": 750000},
    "Kabel xlr 5m": {"jumlah": 50, "harga": 150000},
    "Stand Speaker": {"jumlah": 15, "harga": 350000}
}

login_status = False  

def tampilkan_header():
    print("\nSelamat datang di Ronalvi Audio")
    print("-----------------------------")
    print("1. Registrasi")
    print("2. Masuk")
    print("3. Keluar")

def tampilkan_barang():
    """Menampilkan daftar barang"""
    if not barang:
        print("Belum ada barang di daftar.")
    else:
        nomor = 1
        for nama, info in barang.items():
            print(f"{nomor}. Nama  : {nama}")
            print(f"   Jumlah: {info['jumlah']}")
            print(f"   Harga : Rp.{info['harga']}")
            print("   -----------")
            nomor += 1

def tambah_barang(nama, jumlah, harga):
    """Menambah barang baru"""
    global barang
    barang[nama] = {"jumlah": jumlah, "harga": harga}
    print(f"Barang '{nama}' berhasil ditambahkan.")

def ubah_barang(nama_lama, nama_baru, jumlah_baru, harga_baru):
    """Mengubah data barang"""
    global barang
    barang.pop(nama_lama)
    barang[nama_baru] = {"jumlah": jumlah_baru, "harga": harga_baru}
    print("Barang berhasil diubah.")

def registrasi():
    """Prosedur registrasi pengguna baru"""
    while True:
        usernameBaru = input("Masukkan username anda : ")
        if usernameBaru in username:
            print("Username telah digunakan, pilih username lain!")
        else:
            username.append(usernameBaru)
            passwordBaru = input("Masukkan password anda : ")
            password.append(passwordBaru)
            tipe = input("Masukkan tipe akun (admin/user): ")
            if tipe not in ["admin", "user", "Admin", "User"]:
                tipe = "user"
            tipe_akun.append(tipe)
            print("Registrasi telah berhasil!")
            break

def hapus_barang():
    """Prosedur untuk menghapus barang"""
    if not barang:
        print("Tidak ada barang untuk dihapus.")
        return
    daftar_nama = list(barang.keys())
    for i in range(len(daftar_nama)):
        print(f"{i+1}. {daftar_nama[i]}")
    try:
        nomor = int(input("Pilih nomor barang yang mau dihapus: "))
        if 1 <= nomor <= len(daftar_nama):
            nama_hapus = daftar_nama[nomor - 1]
            barang.pop(nama_hapus)
            print(f"Barang '{nama_hapus}' berhasil dihapus.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

def hitung_total_barang(index=0, jumlah_seluruh=0):
    """Menghitung total semua jumlah barang secara rekursif"""
    daftar = list(barang.values())
    if index == len(daftar):
        return jumlah_seluruh
    return hitung_total_barang(index + 1, jumlah_seluruh + daftar[index]["jumlah"])

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

        if not username:
            print("Belum ada akun yang terdaftar!")
            continue

        loginUsername = input("Masukkan username anda : ")
        loginPassword = input("Masukkan password anda : ")

        if loginUsername in username:
            user_index = username.index(loginUsername)
            if password[user_index] == loginPassword:
                tipe = tipe_akun[user_index]
                print(f"\nLogin berhasil sebagai {tipe}!")
                login_status = True

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
                            if tipe not in ["admin", "Admin"]:
                                print("Hanya admin yang boleh menambah barang!")
                                continue
                            nama = input("Nama barang : ")
                            jumlah = int(input("Jumlah barang : "))
                            harga = int(input("Harga barang : "))
                            tambah_barang(nama, jumlah, harga)

                        elif pilihan_barang == '2':
                            tampilkan_barang()

                        elif pilihan_barang == '3':
                            if tipe not in ["admin", "Admin"]:
                                print("Hanya admin yang boleh mengubah barang!")
                                continue
                            tampilkan_barang()
                            nama_lama = input("Masukkan nama barang lama : ")
                            if nama_lama in barang:
                                nama_baru = input("Nama baru : ")
                                jumlah_baru = int(input("Jumlah baru : "))
                                harga_baru = int(input("Harga baru : "))
                                ubah_barang(nama_lama, nama_baru, jumlah_baru, harga_baru)
                            else:
                                print("Nama barang tidak ditemukan.")

                        elif pilihan_barang == '4':
                            if tipe not in ["admin", "Admin"]:
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

            else:
                print("Password salah.")
        else:
            print("Username tidak ditemukan.")

    elif pilihan == "3":
        print("Program berhenti!")
        break

    else:
        print("Pilihan tidak valid!")