username = []
password = []
nama_item = ["Speaker Yamaha DBR 15", "Midas M32", "Shure SM 58", "Kabel xlr 5m", "Stand Speaker"]
jumlah_item = [10, 5, 20, 50, 15]
harga_item = [5000000, 3000000, 750000, 150000, 350000]

while True :
    print("Selamat datang di Ronalvi Audio")
    print("-----------------------------")
    print("1. Registrasi")
    print("2. Masuk")
    print("3. Keluar")

    pilihan = input("Pilihan anda : ")

    if pilihan == "1" :
        print("\nHalaman Registrasi")
        print("------------------")

        while True :
            usernameBaru = input("Masukkan username anda : ")
            if usernameBaru in username :
                print("username telah digunakan, pilih username lain!")
            else :
                username.append(usernameBaru)
                passwordBaru = input("Masukkan password anda : ")
                password.append(passwordBaru)
                print("Registrasi telah berhasil")
                print("-------------------------")
                break
    
    elif pilihan == "2" :
        print("\nHalaman Masuk")
        print("-------------")

        if not username :
            print("Belum ada akun yang terdaftar!")
            continue

        loginUsername = input("Masukkan username anda : ")
        loginPassword = input("Masukkan password anda : ")

        if loginUsername in username :
            user_index = username.index(loginUsername)

            if password[user_index] == loginPassword :
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
                        
                        nama_item.append(nama)
                        jumlah_item.append(jumlah)
                        harga_item.append(harga)
                        print(f"Barang '{nama}' berhasil ditambah.")

                    elif pilihan_barang == '2':
                        print("\nDaftar Barang")
                        print("----------------")
                        if not nama_item:
                            print("Belum ada barang di daftar.")
                        else:
                            for i in range(len(nama_item)):
                                print(f"{i+1}. Nama  : {nama_item[i]}")
                                print(f"   Jumlah: {jumlah_item[i]}")
                                print(f"   Harga : Rp.{harga_item[i]}")
                                print("   -----------")

                    elif pilihan_barang == '3':
                        print("\nUbah Barang")
                        print("--------------")
                        if not nama_item:
                            print("Tidak ada barang untuk diubah.")
                        else:
                            for i in range(len(nama_item)):
                                print(f"{i+1}. {nama_item[i]}")
                            
                            nomor = int(input("Pilih nomor barang yang mau diubah: "))
                            index = nomor - 1

                            if 0 <= index < len(nama_item):
                                nama_baru = input(f"Masukkan nama baru untuk '{nama_item[index]}' : ")
                                jumlah_baru = int(input(f"Masukkan jumlah baru : "))
                                harga_baru = int(input(f"Masukkan harga baru : "))
                                
                                nama_item[index] = nama_baru
                                jumlah_item[index] = jumlah_baru
                                harga_item[index] = harga_baru
                                print("Barang berhasil diubah.")
                            else:
                                print("Nomor barang tidak ada.")

                    elif pilihan_barang == '4':
                        print("\nHapus Barang")
                        print("----------------")
                        if not nama_item:
                            print("Tidak ada barang untuk dihapus.")
                        else:
                            for i in range(len(nama_item)):
                                print(f"{i+1}. {nama_item[i]}")
                            
                            nomor = int(input("Pilih nomor barang yang mau dihapus: "))
                            index = nomor - 1

                            if 0 <= index < len(nama_item):
                                barang_dihapus = nama_item.pop(index)
                                jumlah_item.pop(index)
                                harga_item.pop(index)
                                print(f"Barang '{barang_dihapus}' berhasil dihapus.")
                            else:
                                print("Nomor barang tidak ada.")

                    elif pilihan_barang == '5':
                        break 
                    
                    else:
                        print("Pilihan menu barang tidak ada!")

            else :
                print("Password salah")
        else :
            print("username tidak ditemukan")

    elif pilihan == "3" :
        print("program berhenti!")
        break
    
    else :
        print("pilihan tidak valid!")