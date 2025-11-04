username = []
password = []
tipe_akun = []

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
            if tipe.lower() not in ["admin", "user"]:
                tipe = "user"
            tipe_akun.append(tipe.lower())
            print("Registrasi telah berhasil!")
            break


def login():
    """Prosedur login pengguna"""
    if not username:
        print("Belum ada akun yang terdaftar!")
        return None

    loginUsername = input("Masukkan username anda : ")
    loginPassword = input("Masukkan password anda : ")

    if loginUsername in username:
        user_index = username.index(loginUsername)
        if password[user_index] == loginPassword:
            print(f"\nLogin berhasil sebagai {tipe_akun[user_index]}!")
            return tipe_akun[user_index]
        else:
            print("Password salah.")
    else:
        print("Username tidak ditemukan.")
    return None
