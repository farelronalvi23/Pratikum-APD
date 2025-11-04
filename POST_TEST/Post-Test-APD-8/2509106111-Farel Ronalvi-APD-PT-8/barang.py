from prettytable import PrettyTable

barang = {
    "Speaker Yamaha DBR 15": {"jumlah": 10, "harga": 5000000},
    "Midas M32": {"jumlah": 5, "harga": 3000000},
    "Shure SM 58": {"jumlah": 20, "harga": 750000},
    "Kabel xlr 5m": {"jumlah": 50, "harga": 150000},
    "Stand Speaker": {"jumlah": 15, "harga": 350000}
}


def tampilkan_barang():
    """Menampilkan daftar barang dalam bentuk tabel"""
    if not barang:
        print("Belum ada barang di daftar.")
    else:
        tabel = PrettyTable(["No", "Nama Barang", "Jumlah", "Harga (Rp)"])
        for i, (nama, info) in enumerate(barang.items(), start=1):
            tabel.add_row([i, nama, info['jumlah'], f"Rp {info['harga']:,}"])
        print(tabel)


def tambah_barang(nama, jumlah, harga):
    barang[nama] = {"jumlah": jumlah, "harga": harga}
    print(f"Barang '{nama}' berhasil ditambahkan.")


def ubah_barang(nama_lama, nama_baru, jumlah_baru, harga_baru):
    if nama_lama in barang:
        barang.pop(nama_lama)
        barang[nama_baru] = {"jumlah": jumlah_baru, "harga": harga_baru}
        print("Barang berhasil diubah.")
    else:
        print("Nama barang tidak ditemukan.")


def hapus_barang():
    """Prosedur untuk menghapus barang"""
    if not barang:
        print("Tidak ada barang untuk dihapus.")
        return
    tampilkan_barang()
    daftar_nama = list(barang.keys())
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
