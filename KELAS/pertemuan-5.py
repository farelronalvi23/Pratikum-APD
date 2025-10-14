# # praktikum = ["Mahasiswa", 20, True, 45.10, ['APD',25]]
# # print(praktikum[4][0])

# # studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # print(studyclub)
# # # Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# # studyclub[2] = "AI"
# # print(studyclub)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[3]
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen dengan nilai "Kalkulus"
# matakuliah.remove('Kalkulus')
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# ambil_matkul = matakuliah.pop(2)
# print(matakuliah)
# print(ambil_matkul)

matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
'Orsikom','Basis Data']
# Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
print(matakuliah[1:6:2])