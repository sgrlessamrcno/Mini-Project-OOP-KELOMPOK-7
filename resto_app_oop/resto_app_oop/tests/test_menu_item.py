import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import MenuItem, Makanan, Minuman, Pesanan


class TestMenu(unittest.TestCase):
    def test_kurangi_stok(self):
        m = MenuItem("ABC", "Tes", 1000, 5)
        m.kurangi_stok(3)
        self.assertEqual(m.stok, 2)
        with self.assertRaises(ValueError):
            m.kurangi_stok(10)

    def test_polimorfisme_harga(self):
        self.assertEqual(Minuman("MNM01", "Teh", 5000, 1, "M").hitung_harga(), 5000)
        self.assertEqual(Minuman("MNM02", "Teh", 5000, 1, "L").hitung_harga(), 8000)
        self.assertEqual(Makanan("MKN01", "Nasi", 20000, 1).hitung_harga(), 20000)

    def test_total_pesanan(self):
        p = Pesanan(1, 1)
        p.tambah_item(Makanan("MKN01", "Nasi", 20000, 5), 2)
        p.tambah_item(Minuman("MNM01", "Teh", 5000, 5), 1)
        self.assertEqual(p.total, 45000)


if __name__ == "__main__":
    unittest.main()
