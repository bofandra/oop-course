# Panduan fasilitator — ekstensi Web Framework (opsional)

## Posisi dalam kursus

Materi ini adalah *post-course extension*, bukan modul 17 dan bukan
prasyarat lulus CLO 1–6. Tidak mengubah referensi formal dalam
[SOURCE_BOUNDARY.md](../../SOURCE_BOUNDARY.md). Untuk referensi API,
dokumentasi framework adalah bahan implementasi opsional, bukan buku
teori ketiga untuk silabus wajib.

## Target pertemuan opsional (3 sesi x 90 menit)

| Sesi | Demonstrasi | Bukti pemahaman |
|---|---|---|
| 1 | OOA → class diagram → pure-python | Mahasiswa bisa menjelaskan entity, invariant, collaborator dan composition |
| 2 | FastAPI vs Flask dengan domain sama | Mahasiswa membedakan HTTP adapter dari domain behavior |
| 3 | Django ORM adapter dan tests | Mahasiswa menunjukkan polymorphism, identity vs persisted row |

## Rencana diskusi

1. Minta mahasiswa mendefinisikan objek `Book` dan invariant sebelum
   membuka file framework.
2. Gambarkan relasi **service uses repository** (has-a) dibandingkan
   **InMemoryRepository implements Repository** (is-a).
3. Peragakan `Book.revise()` gagal secara atomik pada objek saat author kosong.
4. Ganti `KeepCaseTitlePolicy` dengan `CompactWhitespaceTitlePolicy`.
5. Jalankan suite domain; baru kemudian suite HTTP adapters.
6. Pada Django, minta jelaskan dua class bernama Book yang berbeda dan
   kapan pemisahan itu bermanfaat/terlalu kompleks.

## Observasi formatif (bukan nilai wajib)

- Dapat menunjuk exact class + method untuk masing-masing tanggung jawab.
- Tidak menaruh `HTTPException` atau `JsonResponse` pada `Book`.
- Memahami bahwa abstract class tidak otomatis berarti desain bagus.
- Bisa menjelaskan risiko alias reference dan proses in-memory vs DB.
- Mampu menunjukkan tes invariant, tes service dan tes adapter.

## Saran penilaian tambahan (opsional)

Gunakan rubrik empat kriteria secara formatif: domain modeling,
justifikasi OOP, test evidence, dan argumentasi trade-off. Setiap
kriteria dapat dinilai 0–3: belum muncul, parsial, tepat, dan mampu
mempertahankan desain terhadap perubahan kebutuhan. Jangan jadikan
pengenalan web framework syarat tersembunyi asesmen utama.

## Referensi praktikum

- [Panduan OOP-first](OOP_LEARNING_BRIDGE.md)
- [Matriks 16 modul](OOP_CONCEPT_MAPPING.md)
- [Komparasi dan diagram](ARCHITECTURE_COMPARISON.md)
- [Latihan pemula](exercises/beginner.md)
- [Latihan menengah](exercises/intermediate.md)
- [Latihan lanjut](exercises/advanced.md)
