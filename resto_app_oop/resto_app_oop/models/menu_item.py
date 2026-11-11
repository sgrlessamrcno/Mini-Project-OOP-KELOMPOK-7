class MenuItem:
    def __init__(self, kode, nama, harga, stok=0):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def hitung_harga(self):
        return self.harga

    def kurangi_stok(self, jumlah):
        if jumlah > self.stok:
            raise ValueError(f"Stok {self.nama} tidak cukup (sisa {self.stok})")
        self.stok -= jumlah

    def tambah_stok(self, jumlah):
        self.stok += jumlah

    def __str__(self):
        return f"[{self.kode}] {self.nama:<18} Rp{self.hitung_harga():>8,} (stok {self.stok})"
