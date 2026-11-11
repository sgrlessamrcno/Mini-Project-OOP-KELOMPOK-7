from models import Makanan, Minuman, Pesanan
from utils import valid_kode, valid_jumlah

print("Kode 'MKN01' valid?", valid_kode("MKN01"))
print("Jumlah 0 valid?", valid_jumlah(0))

es = Minuman("MNM09", "Es Kopi", 15000, 10, ukuran="L")
nasi = Makanan("MKN09", "Nasi Uduk", 18000, 10)
p = Pesanan(1, 5)
p.tambah_item(es, 2)
p.tambah_item(nasi, 1)
print("Total pesanan:", p.total)
