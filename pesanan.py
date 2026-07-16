"""
Modul: pesanan.py
Mengurus pesanan pelanggan.
"""

def proses_pesanan(inventori, pesanan_pelanggan):
    """
    Memproses pesanan pelanggan.

    Parameter:
        inventori (dict)
        pesanan_pelanggan (list)

    Return:
        tuple
    """

    jumlah_bil = 0.0
    buku_gagal = []

    for id_buku in pesanan_pelanggan:

        if id_buku not in inventori:

            print(f"Ralat: Buku {id_buku} tidak wujud!")
            buku_gagal.append(id_buku)

        else:

            tajuk, harga, stok = inventori[id_buku]

            if stok > 0:

                jumlah_bil += harga

                inventori[id_buku] = (
                    tajuk,
                    harga,
                    stok - 1
                )

            else:

                print(f"Maaf, buku {tajuk} telah habis stok!")
                buku_gagal.append(id_buku)

    return jumlah_bil, buku_gagal