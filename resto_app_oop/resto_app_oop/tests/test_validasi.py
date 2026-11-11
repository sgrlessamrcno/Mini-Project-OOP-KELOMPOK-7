import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import valid_kode, valid_jumlah, valid_meja, valid_metode, valid_uang


class TestValidasi(unittest.TestCase):
    def test_kode(self):
        self.assertTrue(valid_kode("MKN01"))
        self.assertFalse(valid_kode("M!"))
        self.assertFalse(valid_kode(123))

    def test_jumlah(self):
        self.assertTrue(valid_jumlah(5))
        self.assertFalse(valid_jumlah(0))
        self.assertFalse(valid_jumlah(100))

    def test_meja(self):
        self.assertTrue(valid_meja(10))
        self.assertFalse(valid_meja(51))

    def test_metode_uang(self):
        self.assertTrue(valid_metode("qris"))
        self.assertFalse(valid_metode("kredit"))
        self.assertTrue(valid_uang(1000))
        self.assertFalse(valid_uang(-5))


if __name__ == "__main__":
    unittest.main()
