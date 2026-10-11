# Hanoi menggunakan Python

Nama: Ananda Rizky Muntazar Muthahhari

Tugas 2 - Membuat code snippet yang dapat menyelesaikan permainan pada soal gambar di E-Learning
<img width="255" height="274" alt="image (3)" src="https://github.com/user-attachments/assets/b0e8adcc-1b4d-4165-9f71-aa40ebd6aafe" />


## Deskripsi
Program ini menyelesaikan permainan Tower of Hanoi dengan memindahkan 3 piringan dari tiang A ke tiang C menggunakan tiang B sebagai bantuan.

## Algoritma yang digunakan
Program menggunakan **rekursi (recursion)**, yaitu teknik ketika sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan bagian masalah yang lebih kecil.

## Aturan permainan
1. Hanya satu piringan yang boleh dipindahkan dalam satu langkah.
2. Hanya piringan paling atas yang boleh dipindahkan.
3. Piringan besar tidak boleh diletakkan di atas piringan yang lebih kecil.

## Cara kerja program
1. Pindahkan piringan yang lebih kecil ke tiang bantuan.
2. Pindahkan piringan terbesar ke tiang tujuan.
3. Pindahkan piringan dari tiang bantuan ke tiang tujuan.
4. Ulangi proses sampai semua piringan berada di tiang C.

## Cara menjalankan
Pastikan Python sudah terpasang, lalu jalankan perintah berikut di terminal:

```bash
python hanoi.py
```

## Contoh output
```text
Solusi Hanoi:
Pindahkan piringan 1 dari A ke C
Pindahkan piringan 2 dari A ke B
Pindahkan piringan 1 dari C ke B
Pindahkan piringan 3 dari A ke C
Pindahkan piringan 1 dari B ke A
Pindahkan piringan 2 dari B ke C
Pindahkan piringan 1 dari A ke C
```

## Jumlah langkah
Jumlah langkah minimum dihitung dengan rumus `2^n - 1`. Untuk 3 piringan: `2^3 - 1 = 7` langkah.

## Kesimpulan
Rekursi membantu menyelesaikan masalah Hanoi secara bertahap dengan membagi masalah menjadi bagian-bagian yang lebih kecil.
