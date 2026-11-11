from .menu_item import MenuItem


class Makanan(MenuItem):
    def __init__(self, kode, nama, harga, stok=0, tingkat_pedas=0):
        super().__init__(kode, nama, harga, stok)
        self.tingkat_pedas = tingkat_pedas  # 0 = tidak pedas

    def __str__(self):
        return super().__str__() + f" | pedas: {self.tingkat_pedas}"


class Minuman(MenuItem):
    TAMBAHAN_LARGE = 3000

    def __init__(self, kode, nama, harga, stok=0, ukuran="M"):
        super().__init__(kode, nama, harga, stok)
        self.ukuran = ukuran  # "M" atau "L"

    def hitung_harga(self):
        return self.harga + (self.TAMBAHAN_LARGE if self.ukuran == "L" else 0)

    def __str__(self):
        return super().__str__() + f" | ukuran: {self.ukuran}"
