from models import Pesanan, Transaksi
from utils import valid_metode, valid_uang

PAJAK = 0.10


class PembayaranService:
    def __init__(self, pesanan_service):
        self._pesanan_service = pesanan_service
        self._riwayat = []

    def bayar(self, id_pesanan, metode, uang):
        if not valid_metode(metode):
            raise ValueError("Metode harus TUNAI / QRIS / DEBIT")
        if not valid_uang(uang):
            raise ValueError("Jumlah uang tidak valid")
        pesanan = self._pesanan_service.get_pesanan(id_pesanan)
        if pesanan.status != Pesanan.STATUS_BARU or not pesanan.items:
            raise ValueError("Pesanan tidak dapat dibayar")

        subtotal = pesanan.total
        pajak = int(subtotal * PAJAK)
        total = subtotal + pajak
        if uang < total:
            raise ValueError(f"Uang kurang: total Rp{total:,}")

        trx = Transaksi(pesanan, metode.upper(), subtotal, pajak, total, uang)
        pesanan.status = Pesanan.STATUS_LUNAS
        self._riwayat.append(trx)
        return trx

    def riwayat(self):
        return list(self._riwayat)
