"""
Modul: pembersihan.py
Fungsi untuk membersihkan data mentah buku.
"""

def bersihkan_data(data_mentah):
    """
    Membersihkan data mentah dan menukarkannya kepada senarai tuple.

    Parameter:
        data_mentah (str): Data buku dalam bentuk string.

    Return:
        list: Senarai tuple (id_buku, tajuk, harga, stok)
    """

    # Buang ruang kosong di awal dan akhir
    data_mentah = data_mentah.strip()

    # Split ikut koma
    senarai_buku = data_mentah.split(",")

    # Simpan data yang telah dibersihkan
    data_bersih = []

    # Proses setiap rekod buku
    for buku in senarai_buku:

        buku = buku.strip()

        info = buku.split(":")

        if len(info) != 4:
            print("Data tidak lengkap:", buku)
            continue

        try:

            # Bersihkan ID Buku
            id_buku = info[0].strip().upper()

            # Bersihkan Tajuk Buku
            tajuk = info[1]

            # Buang literal "\n"
            tajuk = tajuk.replace("\\n", " ")

            # Buang newline sebenar
            tajuk = tajuk.replace("\n", " ")

            # Buang tab jika ada
            tajuk = tajuk.replace("\t", " ")

            # Buang ruang kosong berlebihan
            tajuk = " ".join(tajuk.split())

            # Tukar kepada Title Case
            tajuk = tajuk.title()

            # Tukar harga kepada float
            harga = float(info[2])

            # Tukar stok kepada int
            stok = int(info[3])

            # Simpan ke dalam list
            data_bersih.append((id_buku, tajuk, harga, stok))

        except ValueError:
            print("Data rosak:", buku)

    return data_bersih