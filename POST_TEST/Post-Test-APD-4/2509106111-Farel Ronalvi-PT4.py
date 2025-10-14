username = "Ronalvi"
password = "111"  

login_attempts = 0
login_success = False

while login_attempts < 3:
    input_username = input("Masukkan Username: ")
    input_password = input("Masukkan Password: ")

    if input_username == username and input_password == password:
        print("Login berhasil!\n")
        login_success = True
        break
    else:
        login_attempts += 1
        print(f"Login gagal. Percobaan ke-{login_attempts}\n")

if not login_success:
    print("Login gagal 3 kali. Program berhenti.")
else:
    total_bayar = 0
    jenis_tiket = ""
    jumlah_tiket = 0

    while True:
        print("=== Menu Pembelian Tiket ===")
        print("1. Tiket Reguler - Rp 50.000")
        print("2. Tiket VIP     - Rp 100.000")
        print("3. Tiket VVIP    - Rp 150.000")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == "1":
            harga = 50000
            jenis_tiket = "Reguler"
        elif pilihan == "2":
            harga = 100000
            jenis_tiket = "VIP"
        elif pilihan == "3":
            harga = 150000
            jenis_tiket = "VVIP"
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan layanan Bioskop kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.\n")
            continue

        jumlah = input(f"Masukkan jumlah tiket {jenis_tiket}: ")
        if jumlah.isdigit():
            jumlah = int(jumlah)
            jumlah_tiket += jumlah
            subtotal = 0
            for i in range(jumlah):
                subtotal += harga
            total_bayar += subtotal
            print(f"\nAnda membeli {jumlah} tiket {jenis_tiket} dengan subtotal Rp {subtotal:,}\n")
        else:
            print("Input jumlah tiket harus berupa angka.\n")

    print("\n=== Rincian Pembelian ===")
    print(f"Total tiket dibeli: {jumlah_tiket}")
    print(f"Total bayar sebelum diskon: Rp {total_bayar:,}")

    if total_bayar >= 300000:
        potongan = total_bayar * 0.12
        total_bayar -= potongan
        print(f"Potongan 12%: Rp {potongan:,}")
    elif total_bayar >= 1500000:
        potongan = total_bayar * 0.08
