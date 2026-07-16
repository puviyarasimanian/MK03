"""
Modul: inventori.py
Fungsi membina inventori dan mengemaskini stok.
"""

def bina_inventori(data_bersih):
    """
    Membina dictionary inventori.

    Parameter:
        data_bersih (list)

    Return:
        dict
    """

    inventori = {}

    for item in data_bersih:
        inventori[item[0]] = (item[1], item[2], item[3])

    return inventori


def kemaskini_stok(inventori, id_buku, jumlah_tambahan):
    """
    Menambah stok buku secara dinamik.

    Parameter:
        inventori (dict)
        id_buku (str)
        jumlah_tambahan (int)

    Return:
        dict
    """

    if id_buku in inventori:

        tajuk, harga, stok = inventori[id_buku]

        inventori[id_buku] = (
            tajuk,
            harga,
            stok + jumlah_tambahan
        )

        print(f"Stok {id_buku} berjaya dikemaskini.")

    else:
        print("Ralat: ID Buku tidak dijumpai.")

    return inventori