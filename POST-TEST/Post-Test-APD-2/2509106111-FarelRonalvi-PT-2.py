print("SELAMAT DATANG DI FAREL ELEKTRONIK")
print("Masukkan Nama anda: ")
nama = input()
print("Masukkan NIM anda: ")
nim = int(input())
print("Pilihan Brand Laptop :")
print("1. Acer")
print("2. Asus")
print("3. Lenovo")
print("Budget jpembelian laptop anda: ")
hargaAwal = int(input())
diskonAcer = hargaAwal * float(5) / 100
diskonAsus = hargaAwal * float(7) / 100
diskonLenovo = hargaAwal * float(10) / 100
hargaAkhirAcer = hargaAwal - diskonAcer
hargaAkhirAsus = hargaAwal - diskonAsus
hargaAkhirLenovo = hargaAwal - diskonLenovo
print(nama + " " + "dengan NIM " + str(nim) + " " + "ingin membeli laptop dengan budget " + str(hargaAwal))
print("Jika " + nama + " " + "membeli laptop Acer anda harus membayar Rp" + str(hargaAkhirAcer) + " " + "setelah mendapat diskon 5%")
print("Jika " + nama + " " + "membeli laptop Asus anda harus membayar Rp" + str(hargaAkhirAsus) + " " + "setelah mendapat diskon 7%")
print("Jika " + nama + " " + "membeli laptop Lenovo anda harus membayar Rp" + str(hargaAkhirLenovo) + " " + "setelah mendapat diskon 10%")
