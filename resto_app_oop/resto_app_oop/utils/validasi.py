METODE_BAYAR = ("TUNAI", "QRIS", "DEBIT")


def valid_kode(kode):
    """Kode menu: 3-6 karakter huruf/angka, contoh 'MKN01'."""
    return isinstance(kode, str) and kode.isalnum() and 3 <= len(kode) <= 6


def valid_jumlah(jumlah):
    return isinstance(jumlah, int) and 1 <= jumlah <= 99


def valid_meja(nomor):
    return isinstance(nomor, int) and 1 <= nomor <= 50


def valid_metode(metode):
    return isinstance(metode, str) and metode.upper() in METODE_BAYAR


def valid_uang(uang):
    return isinstance(uang, (int, float)) and uang > 0
