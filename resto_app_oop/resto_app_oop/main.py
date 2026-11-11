from models import Makanan, Minuman
from services import PesananService, PembayaranService


def data_awal():
    return [
        Makanan("MKN01", "Nasi Goreng", 25000, 20, tingkat_pedas=2),
        Makanan("MKN02", "Soto Ayam", 22000, 15, tingkat_pedas=1),
        Makanan("MKN03", "Ayam Bakar", 30000, 10, tingkat_pedas=1),
        Minuman("MNM01", "Es Teh", 6000, 50, ukuran="M"),
        Minuman("MNM02", "Jus Jeruk", 12000, 30, ukuran="L"),
    ]


def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError("Input harus berupa angka")


def main():
    pesanan_svc = PesananService(data_awal())
    bayar_svc = PembayaranService(pesanan_svc)

    menu_utama = """
=== RESTO TERPADU ===
1. Lihat menu
2. Buat pesanan baru
3. Tambah item ke pesanan
4. Lihat pesanan
5. Bayar pesanan
6. Batalkan pesanan
0. Keluar"""

    while True:
        print(menu_utama)
        pilih = input("Pilih: ").strip()
        try:
            if pilih == "1":
                for m in pesanan_svc.daftar_menu():
                    print(m)
            elif pilih == "2":
                p = pesanan_svc.buat_pesanan(input_int("Nomor meja: "))
                print(f"Pesanan #{p.id} dibuat untuk meja {p.nomor_meja}")
            elif pilih == "3":
                idp = input_int("ID pesanan: ")
                kode = input("Kode menu: ").strip().upper()
                pesanan_svc.tambah_item(idp, kode, input_int("Jumlah: "))
                print("Item ditambahkan.")
            elif pilih == "4":
                for p in pesanan_svc.semua_pesanan():
                    print(f"#{p.id} meja {p.nomor_meja} [{p.status}] total Rp{p.total:,}")
                    for i in p.items:
                        print(f"   - {i.menu.nama} x{i.jumlah}")
            elif pilih == "5":
                idp = input_int("ID pesanan: ")
                metode = input("Metode (TUNAI/QRIS/DEBIT): ")
                trx = bayar_svc.bayar(idp, metode, input_int("Uang dibayar: "))
                print(trx.struk())
            elif pilih == "6":
                pesanan_svc.batalkan(input_int("ID pesanan: "))
                print("Pesanan dibatalkan.")
            elif pilih == "0":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak dikenal.")
        except (ValueError, KeyError) as e:
            print(f"[Error] {e}")


if __name__ == "__main__":
    main()
