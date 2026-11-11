from models import Pesanan
from utils import valid_kode, valid_jumlah, valid_meja


class PesananService:
    def __init__(self, daftar_menu=None):
        self._menu = {m.kode: m for m in (daftar_menu or [])}
        self._pesanan = {}
        self._counter = 0

    def tambah_menu(self, menu):
        self._menu[menu.kode] = menu

    def daftar_menu(self):
        return list(self._menu.values())

    def cari_menu(self, kode):
        if not valid_kode(kode) or kode not in self._menu:
            raise KeyError(f"Menu '{kode}' tidak ditemukan")
        return self._menu[kode]

    def buat_pesanan(self, nomor_meja):
        if not valid_meja(nomor_meja):
            raise ValueError("Nomor meja tidak valid (1-50)")
        self._counter += 1
        p = Pesanan(self._counter, nomor_meja)
        self._pesanan[p.id] = p
        return p

    def tambah_item(self, id_pesanan, kode, jumlah):
        if not valid_jumlah(jumlah):
            raise ValueError("Jumlah tidak valid (1-99)")
        pesanan = self.get_pesanan(id_pesanan)
        if pesanan.status != Pesanan.STATUS_BARU:
            raise ValueError("Pesanan sudah tidak bisa diubah")
        menu = self.cari_menu(kode)
        menu.kurangi_stok(jumlah)
        pesanan.tambah_item(menu, jumlah)
        return pesanan

    def batalkan(self, id_pesanan):
        pesanan = self.get_pesanan(id_pesanan)
        if pesanan.status != Pesanan.STATUS_BARU:
            raise ValueError("Hanya pesanan BARU yang bisa dibatalkan")
        for i in pesanan.items:
            i.menu.tambah_stok(i.jumlah)
        pesanan.status = Pesanan.STATUS_BATAL

    def get_pesanan(self, id_pesanan):
        if id_pesanan not in self._pesanan:
            raise KeyError(f"Pesanan #{id_pesanan} tidak ada")
        return self._pesanan[id_pesanan]

    def semua_pesanan(self):
        return list(self._pesanan.values())
