import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Makanan, Pesanan
from services import PesananService


class TestPesananService(unittest.TestCase):
    def setUp(self):
        self.nasi = Makanan("MKN01", "Nasi", 20000, 5)
        self.svc = PesananService([self.nasi])

    def test_tambah_item_kurangi_stok(self):
        p = self.svc.buat_pesanan(3)
        self.svc.tambah_item(p.id, "MKN01", 2)
        self.assertEqual(self.nasi.stok, 3)
        self.assertEqual(p.total, 40000)

    def test_stok_tidak_cukup(self):
        p = self.svc.buat_pesanan(3)
        with self.assertRaises(ValueError):
            self.svc.tambah_item(p.id, "MKN01", 9)

    def test_menu_tidak_ada(self):
        p = self.svc.buat_pesanan(3)
        with self.assertRaises(KeyError):
            self.svc.tambah_item(p.id, "XXX99", 1)

    def test_batalkan_kembalikan_stok(self):
        p = self.svc.buat_pesanan(3)
        self.svc.tambah_item(p.id, "MKN01", 2)
        self.svc.batalkan(p.id)
        self.assertEqual(self.nasi.stok, 5)
        self.assertEqual(p.status, Pesanan.STATUS_BATAL)

    def test_meja_invalid(self):
        with self.assertRaises(ValueError):
            self.svc.buat_pesanan(0)


if __name__ == "__main__":
    unittest.main()
