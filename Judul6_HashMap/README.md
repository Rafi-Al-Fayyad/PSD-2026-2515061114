Tugas Akhir Percobaan 6

Program ini merupakan implementasi Hash Map dengan metode Separate Chaining pada sistem server game online. Setiap pemain disimpan menggunakan ID pemain sebagai key dan data pemain (nama, level, dan gold) sebagai value. Hash map digunakan untuk mempercepat proses penyimpanan, pencarian, pembaruan, dan penghapusan data pemain. Ketika terjadi collision (dua atau lebih ID pemain menghasilkan indeks hash yang sama), data pemain disimpan dalam bentuk linked list pada server yang sama menggunakan metode Separate Chaining.

<img width="1182" height="4572" alt="TA 6" src="https://github.com/user-attachments/assets/b736b60e-e9df-48cd-8596-0f5ff430efb2" />

1.	Mendefinisikan class Node yang digunakan untuk membuat node pada linked list untuk metode Separate Chaining.
2.	Mendefinisikan method __init__ sebagai constructor untuk class Node.
3.	Menyimpan ID pemain ke dalam atribut key.
4.	Menyimpan data pemain (nama, level, dan gold) ke dalam atribut value.
5.	Membuat pointer next dengan nilai awal None untuk menghubungkan node berikutnya.
6.	
7.	Mendefinisikan class HashMapSeparateChaining untuk mengelola data pemain menggunakan Hash Map.
8.	Mendefinisikan constructor __init__ pada class HashMapSeparateChaining.
9.	Menyimpan ukuran hash table ke dalam atribut SIZE.
10.	Membuat hash table berupa list yang berisi nilai awal None.
11.	
12.	Mendefinisikan fungsi hash_function() untuk menghitung indeks penyimpanan berdasarkan key.
13.	Mengembalikan hasil perhitungan hash menggunakan operasi modulo terhadap ukuran tabel.
14.	
15.	Mendefinisikan fungsi insert() untuk menambahkan data pemain ke hash table.
16.	Menghitung indeks penyimpanan menggunakan fungsi hash.
17.	Menyimpan node pertama pada bucket yang dituju ke variabel current.
18.	
19.	Melakukan perulangan selama masih terdapat node pada bucket tersebut.
20.	Mengecek apakah key yang dimasukkan sudah ada.
21.	Jika key ditemukan, data pemain diperbarui dengan value baru.
22.	Menghentikan proses insert setelah update selesai.
23.	Menggeser pointer ke node berikutnya.
24.	
25.	Membuat node baru menggunakan Node(key, value).
26.	Menghubungkan node baru dengan node pertama yang ada pada bucket tersebut.
27.	Menjadikan node baru sebagai head pada bucket yang bersangkutan.
28.	
29.	Mendefinisikan fungsi search() untuk mencari data pemain berdasarkan ID.
30.	Menghitung indeks bucket menggunakan fungsi hash.
31.	Menyimpan node pertama pada bucket ke variabel current.
32.	
33.	Melakukan perulangan selama node masih ada.
34.	Mengecek apakah key yang dicari sama dengan key pada node saat ini.
35.	Jika ditemukan, mengembalikan node tersebut.
36.	Menggeser pointer ke node berikutnya.
37.	
38.	Mengembalikan None jika data tidak ditemukan.
39.	
40.	Mendefinisikan fungsi remove_key() untuk menghapus data pemain berdasarkan ID.
41.	Menghitung indeks bucket menggunakan fungsi hash.
42.	Menyimpan node pertama bucket ke variabel current.
43.	Membuat variabel prev dengan nilai awal None untuk menyimpan node sebelumnya.
44.	
45.	Melakukan perulangan selama node masih ada.
46.	Mengecek apakah key pada node sama dengan key yang akan dihapus.
47.	Mengecek apakah node yang dihapus merupakan node pertama pada bucket.
48.	Jika benar, head bucket dipindahkan ke node berikutnya.
49.	Jika bukan node pertama,
50.	Pointer node sebelumnya diarahkan ke node setelah node yang dihapus.
51.	Mengembalikan nilai True sebagai tanda data berhasil dihapus.
52.	
53.	Memindahkan prev ke node saat ini.
54.	Memindahkan current ke node berikutnya.
55.	
56.	Mengembalikan nilai False jika data yang dicari tidak ditemukan.
57.	
58.	Mendefinisikan fungsi display() untuk menampilkan seluruh data pemain pada hash table.
59.	Menampilkan judul data pemain.
60.	Melakukan perulangan untuk setiap bucket pada hash table.
61.	Menampilkan nomor bucket dengan label server.
62.	Menyimpan node pertama bucket ke variabel current.
63.	
64.	Melakukan perulangan selama masih terdapat node pada bucket tersebut.
65.	Menampilkan 
66.	ID, nama, 
67.	level, dan gold pemain yang tersimpan pada node.
68.	
69.	
70.	Menggeser pointer ke node berikutnya.
71.	
72.	Menampilkan tulisan NULL sebagai penanda akhir linked list pada bucket.
73.	
74.	
75.	Mendefinisikan fungsi main() sebagai fungsi utama program.
76.	Membuat objek game_server dari class HashMapSeparateChaining.
77.	
78.	Menambahkan data pemain dengan ID 1001 ke hash map.
79.	Menambahkan data pemain dengan ID 1011 ke hash map.
80.	Menambahkan data pemain dengan ID 1021 ke hash map.
81.	Menambahkan data pemain dengan ID 1002 ke hash map.
82.	Menambahkan data pemain dengan ID 1005 ke hash map.
83.	Menambahkan data pemain dengan ID 1015 ke hash map.
84.	Menambahkan data pemain dengan ID 1007 ke hash map.
85.	
86.	Menampilkan seluruh isi hash map menggunakan fungsi display().
87.	
88.	Mencari data pemain dengan ID 1011 menggunakan fungsi search().
89.	
90.	Mengecek apakah data pemain ditemukan.
91.	Menampilkan pesan bahwa pemain ditemukan.
92.	Menampilkan ID pemain yang ditemukan.
93.	Menampilkan nama pemain yang ditemukan.
94.	Menampilkan level pemain yang ditemukan.
95.	Menampilkan jumlah gold pemain yang ditemukan.
96.	Jika data tidak ditemukan,
97.	Menampilkan pesan bahwa pemain tidak ditemukan.
98.	
99.	Menghapus data pemain dengan ID 1011 menggunakan fungsi remove_key().
100. 
101. Menampilkan pesan setelah pemain logout dari server.
102. Menampilkan kembali isi hash map setelah proses penghapusan.
103. 
104. 
105. Mengecek apakah file dijalankan sebagai program utama.
106. Memanggil fungsi main() untuk menjalankan program.

Outuput:
<img width="1761" height="856" alt="image" src="https://github.com/user-attachments/assets/b7ae19f0-eca7-41a4-817a-039e12e3a78a" />
