from datetime import datetime


class Transaksi:
    def __init__(self, pesanan, metode, subtotal, pajak, total, bayar):
        self.pesanan = pesanan
        self.metode = metode
        self.subtotal = subtotal
        self.pajak = pajak
        self.total = total
        self.bayar = bayar
        self.kembalian = bayar - total
        self.waktu = datetime.now()

    def struk(self):
        baris = [f"=== STRUK PESANAN #{self.pesanan.id} (Meja {self.pesanan.nomor_meja}) ==="]
        for i in self.pesanan.items:
            baris.append(f"{i.menu.nama:<18} x{i.jumlah:<3} Rp{i.subtotal:>9,}")
        baris += [
            f"Subtotal : Rp{self.subtotal:,}",
            f"Pajak 10%: Rp{self.pajak:,}",
            f"TOTAL    : Rp{self.total:,}",
            f"Bayar ({self.metode}): Rp{self.bayar:,}",
            f"Kembali  : Rp{self.kembalian:,}",
            self.waktu.strftime("%d-%m-%Y %H:%M:%S"),
        ]
        return "\n".join(baris)
