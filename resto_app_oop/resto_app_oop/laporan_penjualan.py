from models import Makanan, Minuman
from services import PesananService, PembayaranService

svc = PesananService([
    Makanan("MKN01", "Nasi Goreng", 25000, 20),
    Minuman("MNM01", "Es Teh", 6000, 50),
])
bayar = PembayaranService(svc)

for meja, kode, jml in [(1, "MKN01", 2), (2, "MNM01", 3), (3, "MKN01", 1)]:
    p = svc.buat_pesanan(meja)
    svc.tambah_item(p.id, kode, jml)
    bayar.bayar(p.id, "QRIS", 500000)

print("=== LAPORAN PENJUALAN ===")
total = 0
for t in bayar.riwayat():
    print(f"Pesanan #{t.pesanan.id} meja {t.pesanan.nomor_meja}: Rp{t.total:,} ({t.metode})")
    total += t.total
print(f"Total pendapatan: Rp{total:,}")
