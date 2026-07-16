"""
Modul: cadangan.py
Analisis genre menggunakan operasi Set.
"""

def analisis_genre(genre_haziq, genre_siti):
    """
    Menganalisis genre.

    Parameter:
        genre_haziq (set)
        genre_siti (set)

    Return:
        tuple
    """

    sama = genre_haziq.intersection(genre_siti)

    beza = genre_haziq.difference(genre_siti)

    semua_genre = genre_haziq.union(genre_siti)

    return sama, beza, semua_genre