from barang import barang

def hitung_total_barang(index=0, jumlah_seluruh=0):
    """Menghitung total semua jumlah barang secara rekursif"""
    daftar = list(barang.values())
    if index == len(daftar):
        return jumlah_seluruh
    return hitung_total_barang(index + 1, jumlah_seluruh + daftar[index]["jumlah"])