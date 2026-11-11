# Resto Terpadu - Sistem Manajemen Restoran

Aplikasi Command Line Interface (CLI) berbasis Python untuk manajemen pesanan dan transaksi restoran. Proyek ini mengimplementasikan Object-Oriented Programming (OOP) dan arsitektur modular tanpa dependensi eksternal.

## Struktur Direktori

Sistem dibagi ke dalam beberapa modul untuk menjaga pemisahan tanggung jawab (Separation of Concerns):

* `models/` : Entitas domain sistem (MenuItem, Makanan, Minuman, Pesanan, Transaksi).
* `services/` : Lapisan logika bisnis (PesananService, PembayaranService).
* `utils/` : Fungsi utilitas untuk validasi input.
* `tests/` : Rangkaian unit test menggunakan library `unittest`.
* `docs/` : Dokumentasi tambahan dan diagram UML.

## Alur Kerja Sistem

1. Inisialisasi: Sistem memuat data master menu saat dijalankan.
2. Pesanan: Pembuatan ID pesanan baru berdasarkan nomor meja yang valid.
3. Manajemen Stok: Stok item otomatis berkurang saat ditambahkan ke pesanan, dan sistem akan menolak jika stok tidak mencukupi.
4. Pembayaran: Memvalidasi metode (TUNAI/QRIS/DEBIT) dan nominal bayar. Sistem menghitung pajak 10%, mengubah status menjadi lunas, dan mencetak struk.
5. Pembatalan: Pesanan yang belum dibayar dapat dibatalkan, dan sistem akan mengembalikan (rollback) stok item secara otomatis.

## Cara Menjalankan

Aplikasi ini menggunakan Python Standard Library (minimal Python 3.8) sehingga tidak memerlukan instalasi dependensi pihak ketiga.

Jalankan perintah berikut di terminal pada direktori utama proyek:

```bash
# Menjalankan aplikasi utama
python main.py

# Menjalankan script demonstrasi
python demo_package.py
python demo_coupling.py
python laporan_penjualan.py

# Menjalankan seluruh unit test
python -m unittest discover -s tests
```
