# Latihan pemula — Kembali ke class dan invariant

**Prasyarat:** Modul 1–5, 11, 13–14. Materi tambahan opsional.

## Studi kasus

Pemilik perpustakaan tidak ingin judul atau nama pengarang kosong.
Pembaca harus dapat mengubah judul tanpa memegang langsung state internal.

## Tugas

1. Pada pure-python `entities.py`, jelaskan setiap atribut, method,
   property, dan tanggung jawab class `Book`.
2. Buat dua instance buku: samakan title keduanya dan bandingkan `is`
   dengan kesamaan konten. Jelaskan identitas Python vs ID domain.
3. Buktikan `Book.revise("Baru", "   ")` gagal dan state lama utuh.
4. Tambahkan method `change_author(new_author)` pada domain `Book`
   menggunakan mekanisme validasi yang sudah ada.
5. Buat unit test untuk method baru; jalankan kembali `test_domain.py`.

## Evidence yang harus dikumpulkan

- Nama file/method yang diubah dan alasan desain;
- Test untuk valid, invalid, dan state setelah exception;
- Penjelasan 100–200 kata: *mengapa behavior bukan sekadar assignment
  atribut dari luar?*

## Kriteria selesai

- Test domain seluruhnya tetap hijau;
- Tidak membuat dependency web/framework pada `book_domain`;
- Penjelasan membedakan class, instance, identity, state, method;
- Tidak menambahkan inheritance yang tidak dibutuhkan.

Referensi balik: [Modul 4](../../../week-04/) dan
[Modul 13](../../../week-13/).
