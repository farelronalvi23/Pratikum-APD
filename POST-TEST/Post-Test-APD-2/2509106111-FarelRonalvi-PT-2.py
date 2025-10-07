print("=== PEMBELIAN TIKET BIOSKOP ===")
print("1. Reguler  - Rp35.000")
print("2. VIP      - Rp50.000")
print("3. VVIP     - Rp75.000")

pilih = input("Pilih jenis tiket (1/2/3): ")
jumlah = int(input("Masukkan jumlah tiket: "))

if pilih == "1":
    harga = 35000
    jenis = "Reguler"
elif pilih == "2":
    harga = 50000
    jenis = "VIP"
elif pilih == "3":
    harga = 75000
    jenis = "VVIP"
else:
    print("Pilihan tidak valid!")
    exit()

total = harga * jumlah

print("\n=== STRUK PEMBELIAN ===")
print("Jenis Tiket :", jenis)
print("Harga Satuan : Rp", harga)
print("Jumlah Tiket :", jumlah)
print("Total Bayar: Rp",total)