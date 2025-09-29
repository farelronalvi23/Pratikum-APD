nama_terdaftar = "Saiki"
nim_terdaftar = "123456789"

biaya_langganan = 1500000


def login():
    print("=== Selamat Datang Silahkan Langsung Pilih Paket Langganan nya Namun sebelumnya ===")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
   
    if nama == nama_terdaftar and nim == nim_terdaftar:
        print("\nLogin berhasil!\n")
        return True
    else:
        print("\nLogin gagal! Nama atau NIM salah.\n")
        return False


def hitung_total(biaya, admin):
    return biaya + (biaya * admin)


if login():
    print("=== PILIH PAKET LANGGANAN ===")
    print("1. Bronze")
    print("2. Silver")
    print("3. Gold")
    print("4. Platinum")


    pilihan = input("Masukkan pilihan paket (1-4): ")


    if pilihan == "1":
        total = hitung_total(biaya_langganan, 0.01)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket: Bronze")
        print(f"Biaya Langganan: Rp {biaya_langganan:,}")
        print("Biaya Administrasi: 1%")
        print(f"Total Bayar: Rp {int(total):,}")
        print("Keuntungan: Akses dasar ke lagu-lagu populer.")


    elif pilihan == "2":
        total = hitung_total(biaya_langganan, 0.03)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket: Silver")
        print(f"Biaya Langganan: Rp {biaya_langganan:,}")
        print("Biaya Administrasi: 3%")
        print(f"Total Bayar: Rp {int(total):,}")
        print("Keuntungan: Akses lagu premium dan playlist kustom.")


    elif pilihan == "3":
        total = hitung_total(biaya_langganan, 0.05)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket: Gold")
        print(f"Biaya Langganan: Rp {biaya_langganan:,}")
        print("Biaya Administrasi: 5%")
        print(f"Total Bayar: Rp {int(total):,}")
        print("Keuntungan: Akses lagu premium, playlist kustom, dan mode offline.")


    elif pilihan == "4":
        total = hitung_total(biaya_langganan, 0.07)
        print("\n=== DETAIL PEMBAYARAN ===")
        print("Paket: Platinum")
        print(f"Biaya Langganan: Rp {biaya_langganan:,}")
        print("Biaya Administrasi: 7%")
        print(f"Total Bayar: Rp {int(total):,}")
        print("Keuntungan: Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.")


    else:
        print("\nPilihan tidak valid.")
