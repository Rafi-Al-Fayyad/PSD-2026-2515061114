Tugas Akhir Percobaan 3

Program Mencari Judul Lagu pada Playlist

Program ini digunakan untuk mencari judul lagu di dalam daftar playlist menggunakan algoritma Binary Search. Program menampilkan kumpulan judul lagu yang sudah diurutkan berdasarkan abjad agar proses pencarian dapat dilakukan lebih cepat dan efisien. Pengguna dapat memasukkan judul lagu secara lengkap maupun hanya sebagian kata dari judul lagu. Setelah proses pencarian dilakukan, program akan menampilkan posisi indeks serta judul lagu yang sesuai dengan kata kunci yang dicari.

<img width="1444" height="4292" alt="TA3Searching" src="https://github.com/user-attachments/assets/6683417c-e33d-4fc2-8392-916c290efedf" />

1.	Mendefinisikan fungsi binary_search yang digunakan untuk mencari data lagu dalam array menggunakan metode Binary Search.
2.	Membuat variabel l (left) dengan nilai awal 0 sebagai batas kiri pencarian.
3.	Membuat variabel r (right) dengan nilai n - 1 sebagai batas kanan pencarian.
4.	Membuat list kosong bernama hasil untuk menyimpan index lagu yang ditemukan.
5.	
6.	Memulai perulangan selama batas kiri masih lebih kecil atau sama dengan batas kanan.
7.	Menghitung posisi tengah (median) dari array menggunakan rumus Binary Search.
8.	Menampilkan posisi median dan judul lagu yang sedang dicek.
9.	
10.	Mengecek apakah kata kunci (target) terdapat pada judul lagu di posisi median tanpa membedakan huruf besar dan kecil.
11.	Jika ditemukan, maka index median dimasukkan ke dalam list hasil.
12.	
13.	Membuat variabel i untuk mulai mengecek data di sebelah kiri median.
14.	Memulai perulangan ke kiri selama index masih lebih besar atau sama dengan 0.
15.	Mengecek apakah target terdapat pada lagu di sebelah kiri median.
16.	Jika ditemukan, index lagu tersebut ditambahkan ke list hasil.
17.	Mengurangi nilai i satu per satu agar terus bergerak ke kiri.
18.	
19.	Mengubah nilai i untuk mulai mengecek data di sebelah kanan median.
20.	Melakukan perulangan ke kanan selama index masih kurang dari jumlah data.
21.	Mengecek apakah target terdapat pada lagu di sebelah kanan median.
22.	Jika ditemukan, index lagu tersebut ditambahkan ke list hasil.
23.	Menambah nilai i satu per satu agar terus bergerak ke kanan.
24.	
25.	Menghentikan proses pencarian karena data utama sudah ditemukan.
26.	
27.	Jika target lebih besar dari data di median berdasarkan urutan alfabet.
28.	Menampilkan pesan bahwa pencarian dilanjutkan ke bagian kanan array.
29.	Menggeser batas kiri menjadi m + 1 agar pencarian fokus ke kanan.
30.	Jika target lebih kecil dari data di median.
31.	Menampilkan pesan bahwa pencarian dilanjutkan ke bagian kiri array.
32.	Menggeser batas kanan menjadi m - 1 agar pencarian fokus ke kiri.
33.	
34.	Mengembalikan hasil pencarian dalam keadaan terurut menggunakan sorted().
35.	
36.	Mendefinisikan fungsi main sebagai fungsi utama program.
37.	Membuat list bernama arr yang berisi kumpulan judul lagu playlist.
38.	Judul lagu
39.	Judul lagu
40.	Judul lagu
41.	Judul lagu
42.	Judul lagu
43.	Judul lagu
44.	Judul lagu
45.	Judul lagu
46.	Judul lagu
47.	Judul lagu
48.	Judul lagu
49.	Judul lagu
50.	Judul lagu
51.	Judul lagu
52.	Judul lagu
53.	Judul lagu
54.	Judul lagu
55.	Judul lagu
56.	Judul lagu
57.	Judul lagu
58.	Judul lagu
59.	Judul lagu
60.	Judul lagu
61.	Judul lagu
62.	Judul lagu
63.	Judul lagu
64.	Judul lagu
65.	Judul lagu
66.	Judul lagu
67.	Judul lagu
68.	Judul lagu
69.	Judul lagu
70.	Judul lagu
71.	Judul lagu
72.	Judul lagu
73.	Judul lagu
74.	Judul lagu
75.	Judul lagu
76.	Judul lagu
77.	Judul lagu
78.	Judul lagu
79.	Akhir array
80.	
81.	Menghitung jumlah seluruh data lagu menggunakan fungsi len() lalu menyimpannya ke variabel n.
82.	
83.	Menampilkan judul daftar playlist lagu.
84.	Melakukan perulangan untuk menampilkan semua lagu dalam playlist.
85.	Menampilkan nomor urut beserta judul lagu dari array.
86.	
87.	Meminta user memasukkan judul atau kata lagu yang ingin dicari.
88.	
89.	Memanggil fungsi binary_search untuk mencari lagu berdasarkan input user.
90.	
91.	Mengecek apakah ada hasil pencarian yang ditemukan.
92.	Jika ditemukan, menampilkan pesan bahwa kata yang dicari berhasil ditemukan.
93.	Melakukan perulangan untuk menampilkan semua hasil pencarian.
94.	Menampilkan index dan judul lagu yang cocok dengan kata kunci.
95.	Jika tidak ada hasil pencarian.
96.	Menampilkan pesan bahwa lagu tidak ditemukan.
97.	
98.	
99.	Baris standar Python untuk memastikan program hanya berjalan jika file dieksekusi langsung.
100.	Memanggil fungsi main() untuk menjalankan seluruh program.

Output:
<img width="270" height="494" alt="image" src="https://github.com/user-attachments/assets/aa16c02d-d7cb-417b-9a23-3c307c2124e6" />
<img width="347" height="110" alt="image" src="https://github.com/user-attachments/assets/0eaa3fc4-e1f0-4b59-8562-cfcfc0f6c83c" />

Misal mencari lagu "Thriller":
<img width="387" height="200" alt="image" src="https://github.com/user-attachments/assets/adcb7b94-eea7-4ed4-9ab4-f6201326294f" />

Misal mencari lagu "Duvet":
<img width="383" height="151" alt="image" src="https://github.com/user-attachments/assets/09fa9eef-6419-4750-8907-e1c9e83310bb" />

Video: https://youtu.be/xJt1glRoPJo

Penjabaran rumus binary interpolation:
<img width="1280" height="1020" alt="WhatsApp Image 2026-05-11 at 10 26 39 PM" src="https://github.com/user-attachments/assets/ff9d586a-65b1-45c6-9571-718142bcf06a" />





