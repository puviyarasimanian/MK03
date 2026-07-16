from pembersihan import bersihkan_data
from inventori import bina_inventori, kemaskini_stok
from cadangan import analisis_genre
from pesanan import proses_pesanan

# ====================================
# Bahagian 1 - Data Mentah
# ====================================

data_mentah = """
 b001:mUdaHnya pYtHon:39.90:5 ,
 b010:pYtHon dAn sTaTiStIk:48.00:7 ,
 b011:bElAjAr \n cLoUd:89.90:2 ,
 b002:bElAjAr dAtA sCieNce:49.90:2 ,
 b012:aSas cYbEr sEcUrItY:95.00:0 ,
 b003:aSaS a.i. uNtUk pEmUlA:55.00:0
"""

# Bersihkan data
data_bersih = bersihkan_data(data_mentah)

print("=" * 60)
print("DATA BERSIH")
print("=" * 60)

for item in data_bersih:
    print(item)

# ====================================
# Bahagian 2 - Inventori
# ====================================

inventori = bina_inventori(data_bersih)

print("\n" + "=" * 60)
print("INVENTORI")
print("=" * 60)

for id_buku, maklumat in inventori.items():
    tajuk, harga, stok = maklumat
    print(f"{id_buku:<6} {tajuk:<30} RM{harga:<8.2f} Stok: {stok}")

# Kemaskini stok secara dinamik
kemaskini_stok(inventori, "B002", 10)

print("\nInventori Selepas Kemaskini Stok")

for id_buku, maklumat in inventori.items():
    tajuk, harga, stok = maklumat
    print(f"{id_buku:<6} {tajuk:<30} RM{harga:<8.2f} Stok: {stok}")

# ====================================
# Bahagian 3 - Analisis Genre
# ====================================

genre_haziq = {
    "Teknologi",
    "Sains",
    "Biografi",
    "Fiksyen"
}

genre_siti = {
    "Masakan",
    "Sains",
    "Novel",
    "Teknologi",
    "Kesihatan"
}

sama, beza, semua_genre = analisis_genre(
    genre_haziq,
    genre_siti
)

print("\n" + "=" * 60)
print("ANALISIS SET")
print("=" * 60)

print("Genre Sama           :", sama)
print("Genre Haziq Sahaja   :", beza)
print("Semua Genre          :", semua_genre)

# ====================================
# Bahagian 4 - Pesanan Pelanggan
# ====================================

pesanan_pelanggan = [
    "B001",
    "B003",
    "B001",
    "B999",
    "B010",
    "B011",
    "B012"
]

jumlah_bil, buku_gagal = proses_pesanan(
    inventori,
    pesanan_pelanggan
)

# ====================================
# Keputusan Akhir
# ====================================

print("\n")
print("=" * 60)
print("KEPUTUSAN AKHIR")
print("=" * 60)

print("\nInventori Akhir")

for id_buku, maklumat in inventori.items():
    tajuk, harga, stok = maklumat
    print(f"{id_buku:<6} {tajuk:<30} RM{harga:<8.2f} Stok: {stok}")

print("\nJumlah Bil")
print("RM{:.2f}".format(jumlah_bil))

print("\nBuku Gagal Dibeli")
print(buku_gagal)

print("\nGenre Sama")
print(sama)

print("\nGenre Haziq Sahaja")
print(beza)

print("\nSemua Genre")
print(semua_genre)