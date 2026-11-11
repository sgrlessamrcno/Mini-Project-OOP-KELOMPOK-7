import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Makanan, Pesanan
from services import PesananService, PembayaranService


class TestPembayaran(unittest.TestCase):
    def setUp(self):
        self.ps = PesananService([Makanan("MKN01", "Nasi", 20000, 10)])
        self.bs = PembayaranService(self.ps)
        self.p = self.ps.buat_pesanan(1)
        self.ps.tambah_item(self.p.id, "MKN01", 2)  # 40.000

    def test_bayar_sukses(self):
        t = self.bs.bayar(self.p.id, "tunai", 50000)
        self.assertEqual(t.pajak, 4000)
        self.assertEqual(t.total, 44000)
        self.assertEqual(t.kembalian, 6000)
        self.assertEqual(self.p.status, Pesanan.STATUS_LUNAS)

    def test_uang_kurang(self):
        with self.assertRaises(ValueError):
            self.bs.bayar(self.p.id, "tunai", 10000)

    def test_metode_salah(self):
        with self.assertRaises(ValueError):
            self.bs.bayar(self.p.id, "kredit", 50000)

    def test_tidak_bisa_bayar_dua_kali(self):
        self.bs.bayar(self.p.id, "qris", 50000)
        with self.assertRaises(ValueError):
            self.bs.bayar(self.p.id, "qris", 50000)


if __name__ == "__main__":
    unittest.main()
