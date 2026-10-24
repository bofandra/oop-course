# Latihan menengah — Composition, polymorphism, dan tests

**Prasyarat:** Modul 5–7, 9, 11–15. Opsional.

## Studi kasus

Aplikasi akan memiliki kebijakan normalisasi judul baru: whitespace
berulang dipadatkan. Pengembang ingin menerapkan kebijakan pilihan
tanpa memodifikasi method `BookService.create()`.

## Tugas

1. Bandingkan `KeepCaseTitlePolicy` dengan
   `CompactWhitespaceTitlePolicy`; jelaskan overriding yang terjadi.
2. Buat subkelas `TitlePolicy` bernama `UppercaseTitlePolicy`
   sebagai **eksperimen**. Demonstrasikan melalui constructor service.
3. Buat `SpyRepository` yang mengikuti `BookRepository`
   untuk mencatat method yang dipanggil service saat create/update/delete.
4. Tunjukkan bahwa FastAPI dan Flask menggunakan class domain
   **yang sama**, bukan salinan definisi kelas.
5. Buat tes bahwa judul/pengarang invalid ditolak di tingkat domain,
   meski tidak ada request HTTP.

## Evidence yang harus dikumpulkan

- Diagram `BookService -> TitlePolicy/BookRepository`;
- Uji yang mengganti concrete subclass tanpa mengedit service;
- Penjelasan singkat perbedaan inheritance (is-a) dan composition (has-a);
- Satu contoh alasan untuk **tidak** memakai Strategy pada masalah kecil.

## Kriteria selesai

- Domain tidak mengimpor Flask/FastAPI/Django;
- Dapat menambah policy tanpa mengubah signature method service;
- Assertions membuktikan method subclass benar-benar dipanggil;
- Test HTTP yang sudah ada tetap lulus.

Referensi balik: [Modul 7](../../../week-07/),
[Modul 9](../../../week-09/) dan [Modul 15](../../../week-15/).
