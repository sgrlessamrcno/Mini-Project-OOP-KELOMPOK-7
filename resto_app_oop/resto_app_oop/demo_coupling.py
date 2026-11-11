from models import Makanan
from services import PesananService, PembayaranService


class PesananServicepalsu(PesananService):
    def __init__(self):
        super().__init__([Makanan("TES01", "Menu Tes", 10000, 5)])


svc = PesananServicepalsu()
bayar = PembayaranService(svc)
p = svc.buat_pesanan(1)
svc.tambah_item(p.id, "TES01", 2)
print(bayar.bayar(p.id, "tunai", 50000).struk())
