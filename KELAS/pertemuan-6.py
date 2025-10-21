# # # Membuat set 
# # buah = {"apel", "jeruk", "mangga", "apel"}  
# # print(buah) 

# # angka_ganjil = {1, 3, 5, 7, 9} 
# # for angka in angka_ganjil: 
# #     print(angka)

# Daftar_buku = { 
# "Buku1" : "Bumi Manusia", 
# "Buku2" : "Laut Bercerita" 
# }

# # for attol in Daftar_buku.items():
# #     print(attol)

# Biodata = { 
# "Nama" : "Ananda Daffa Harahap", 
# "NIM" : 2409106050, 
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"], 
# "Mahasiswa_Aktif" : True, 
# "Social Media" : { 

#         "Instagram" : "daffahrhap" 
#     } 
# }

# # print(f"nama saya adalah {Biodata["Nama"]}") 
# # print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
 
# # print(f"nama saya adalah {Biodata.get("Nama")}") 
# # print(Biodata.get("Nama"))


# key = "apel", "jeruk", "mangga" 
 
# value = "Buah favorit"
 
# buah = dict.fromkeys(key, value) 
 
# print(buah) 

Musik = { 
"The Chainsmoker" : ["All we Know", "The Paris"], 
"Alan Walker" : ["Alone", "Lily"], 
"Neffex" : ["Best of Me", "Memories"] 
} 
 
for penyanyi, Album in Musik.items(): 
 print(f"Musik milik {penyanyi} adalah : ") 
 for song in Album: 
  print(song) 
 print("") 