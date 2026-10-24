# Latihan lanjut — Desain ulang untuk kebutuhan nyata

**Prasyarat:** Modul 11–16 + selesainya studi kasus. Opsional.

## Studi kasus

Pengelola menginginkan atribut `year` (tahun terbit) dan persistence.
Aplikasi harus konsisten pada domain dan tiga HTTP adapters.

## Tahap pekerjaan

1. **OOA:** rumuskan invariant `year` (misalnya integer dengan batas
   eksplisit) dan kasus penggunaan create/update/read.
2. **OOD:** revisi class diagram, identifikasi impact ke entity,
   repository port, kedua adapter repository, dan ORM migration.
3. **OOP:** tambah field melalui domain dan adapter, dengan validasi
   yang konsisten dan migrasi Django.
4. **OOT:** buat unit test domain dan integration tests untuk CRUD,
   error, serta persistence setelah service baru dibangun.
5. **Desain:** evaluasi apakah transaksi diperlukan agar update dan
   persistence aman bila request bersamaan.
6. **Refleksi:** bandingkan implementasi memakai rich Django model
   langsung vs domain entity terpisah. Mana yang paling sederhana
   untuk skala aplikasi kecil?

## Kasus uji wajib (pada latihan opsional ini)

- POST/PUT valid pada ketiga adapter menghasilkan JSON dengan `year`.
- Input year tidak valid tidak menyebabkan state yang setengah terubah.
- GET/DELETE terhadap ID tidak ada mengembalikan 404.
- Django berhasil melakukan migration dan persistence (test database).
- Tes domain tidak membutuhkan web framework.

## Evidence

Kumpulkan UML/class diagram, tabel impact perubahan, hasil test
sebelum/sesudah, dan ringkasan trade-off maksimal 1 halaman.

## Perhatian

Contoh asli **belum production-ready**. Jangan menyalin konfigurasi
`SECRET_KEY`, `DEBUG=True`, atau `csrf_exempt` untuk sistem nyata.
API produksi membutuhkan kontrol akses, transaksi dan konfigurasi aman.

Referensi balik: [Modul 14](../../../week-14/) dan
[Modul 16](../../../week-16/).
