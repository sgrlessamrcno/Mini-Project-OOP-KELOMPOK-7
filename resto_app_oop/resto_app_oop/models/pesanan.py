class ItemPesanan:
    def __init__(self, menu, jumlah):
        self.menu = menu
        self.jumlah = jumlah

    @property
    def subtotal(self):
        return self.menu.hitung_harga() * self.jumlah


class Pesanan:
    STATUS_BARU = "BARU"
    STATUS_LUNAS = "LUNAS"
    STATUS_BATAL = "BATAL"

    def __init__(self, id_pesanan, nomor_meja):
        self.id = id_pesanan
        self.nomor_meja = nomor_meja
        self.items = []
        self.status = self.STATUS_BARU

    def tambah_item(self, menu, jumlah):
        self.items.append(ItemPesanan(menu, jumlah))

    @property
    def total(self):
        return sum(i.subtotal for i in self.items)
