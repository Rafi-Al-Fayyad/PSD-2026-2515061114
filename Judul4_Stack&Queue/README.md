Tugas Akhir Percobaan 4

Program Queue Matchmaking Game

Program ini adalah implementasi struktur data queue linked list yang diterapkan pada sistem matchmaking game. Program ini memungkinkan player masuk ke antrean matchmaking menggunakan operasi enqueue, kemudian player paling depan diproses untuk mendapatkan match menggunakan operasi dequeue sesuai konsep FIFO (First In First Out). Selain itu, program juga menyediakan fitur untuk melihat player terdepan dan menampilkan seluruh antrean player yang sedang menunggu pertandingan melalui menu interaktif.

<img width="1710" height="4804" alt="code matchmaking game tugas akhir 4" src="https://github.com/user-attachments/assets/a26ee7b3-ccbd-4f7e-9599-16e6644e276a" />

1.	Mendefinisikan class Node yang digunakan sebagai elemen penyusun linked list pada queue. 
2.	Mendefinisikan method __init__ untuk menginisialisasi objek node saat pertama kali dibuat. 
3.	Menyimpan data player ke dalam atribut data. 
4.	Mengatur pointer next menjadi None karena node baru belum terhubung ke node lain. 
5.	
6.	Mendefinisikan class QueueLinkedList yang digunakan untuk membuat queue berbasis linked list. 
7.	Mendefinisikan method __init__ untuk inisialisasi queue. 
8.	Mengatur front_ptr menjadi None sebagai penanda bahwa bagian depan queue masih kosong. 
9.	Mengatur rear_ptr menjadi None sebagai penanda bahwa bagian belakang queue masih kosong. 
10.	
11.	Mendefinisikan method is_empty() untuk mengecek apakah queue kosong atau tidak. 
12.	Mengembalikan nilai True jika front_ptr bernilai None, yang berarti queue kosong. 
13.	
14.	Mendefinisikan method enqueue() yang berfungsi menambahkan player ke dalam antrean matchmaking. 
15.	Membuat node baru menggunakan data player yang diterima dari parameter. 
16.	
17.	Mengecek apakah queue masih kosong menggunakan method is_empty(). 
18.	Jika queue kosong, maka node baru dijadikan sebagai node paling depan. 
19.	Node baru juga dijadikan sebagai node paling belakang karena baru ada satu data. 
20.	Jika queue tidak kosong, program masuk ke blok else. 
21.	Menghubungkan node terakhir (rear_ptr) ke node baru melalui pointer next. 
22.	Memindahkan posisi rear_ptr ke node baru agar menjadi elemen paling belakang. 
23.	
24.	Menampilkan pesan bahwa player berhasil masuk ke matchmaking.
25.	
26.	Mendefinisikan method dequeue() yang berfungsi menghapus player dari antrean depan. 
27.	Mengecek apakah queue kosong menggunakan method is_empty(). 
28.	Jika queue kosong, program menampilkan pesan bahwa tidak ada player dalam matchmaking. 
29.	Menghentikan proses method menggunakan return. 
30.	
31.	Menyimpan node paling depan ke variabel sementara temp. 
32.	Menampilkan pesan bahwa player berhasil menemukan match dan keluar dari antrean. 
33.	
34.	Memindahkan front_ptr ke node berikutnya sehingga node depan sebelumnya terhapus dari queue. 
35.	
36.	Mengecek apakah setelah dequeue queue menjadi kosong. 
37.	Jika kosong, maka rear_ptr juga diatur menjadi None. 
38.	
39.	Mendefinisikan method peek() untuk melihat player paling depan tanpa menghapusnya. 
40.	Mengecek apakah queue kosong menggunakan is_empty(). 
41.	Jika queue kosong, program menampilkan pesan “Matchmaking kosong”. 
42.	Menghentikan proses method menggunakan return. 
43.	
44.	Menampilkan data player yang berada di posisi paling depan queue. 
45.	
46.	Mendefinisikan method display() untuk menampilkan seluruh isi antrean matchmaking. 
47.	Mengecek apakah queue kosong menggunakan is_empty(). 
48.	Jika queue kosong, program menampilkan pesan “Matchmaking kosong”. 
49.	Menghentikan proses method menggunakan return. 
50.	
51.	Menampilkan judul informasi antrean matchmaking. 
52.	Menyimpan node paling depan ke variabel current untuk proses traversal. 
53.	
54.	Melakukan perulangan selama node saat ini (current) tidak bernilai None. 
55.	Menampilkan data player dari node saat ini diikuti tanda panah (->). 
56.	Memindahkan current ke node berikutnya menggunakan pointer next. 
57.	
58.	Menampilkan tulisan None sebagai penanda akhir linked list. 
59.	
60.	Mendefinisikan fungsi main() sebagai fungsi utama program. 
61.	Membuat objek matchmaking dari class QueueLinkedList. 
62.	Menginisialisasi variabel pilih dengan nilai 0 untuk menyimpan pilihan menu user. 
63.	
64.	Melakukan perulangan selama user belum memilih menu keluar (5). 
65.	Menampilkan judul program matchmaking game online.  
66.	Menampilkan menu untuk player masuk matchmaking. 
67.	Menampilkan menu untuk mencari match atau dequeue. 
68.	Menampilkan menu untuk melihat player paling depan. 
69.	Menampilkan menu untuk menampilkan seluruh antrean. 
70.	Menampilkan menu keluar program. 
71.	
72.	Memulai blok try untuk mengantisipasi kesalahan input user. 
73.	Meminta user memasukkan pilihan menu lalu mengubahnya menjadi integer. 
74.	Jika input bukan angka, program masuk ke blok except. 
75.	Menampilkan pesan bahwa input harus berupa angka. 
76.	Melanjutkan perulangan berikutnya menggunakan continue. 
77.	
78.	Mengecek apakah user memilih menu 1. 
79.	Meminta user memasukkan username player. 
80.	Memanggil method enqueue() untuk menambahkan player ke matchmaking. 
81.	Mengecek apakah user memilih menu 2. 
82.	Memanggil method dequeue() untuk menghapus player paling depan dari antrean. 
83.	Mengecek apakah user memilih menu 3. 
84.	Memanggil method peek() untuk melihat player paling depan. 
85.	Mengecek apakah user memilih menu 4. 
86.	Memanggil method display() untuk menampilkan seluruh antrean matchmaking. 
87.	Mengecek apakah user memilih menu 5. 
88.	Menampilkan pesan bahwa program matchmaking selesai dijalankan. 
89.	Jika pilihan menu tidak sesuai, 
90.	program menampilkan pesan bahwa menu tidak valid.
91.	
92.	
93.	Baris standar Python yang memastikan fungsi main() hanya dijalankan jika file dieksekusi langsung. 
94.	Memanggil fungsi main() untuk menjalankan seluruh program matchmaking game online. 

Output: 
<img width="239" height="109" alt="image" src="https://github.com/user-attachments/assets/47a2acac-2cae-4ec3-a5eb-d84ce2dcd057" />

Pilihan 1, memasukkan username:
<img width="316" height="130" alt="image" src="https://github.com/user-attachments/assets/dff96e68-5ffe-4e01-b461-eec3fbbb201e" />

Pilihan 2, matching:
<img width="359" height="116" alt="image" src="https://github.com/user-attachments/assets/d7133cc4-c17d-488e-a221-d37bca2ceb70" />

Pilihan 2, matching jika queue kosong:
<img width="332" height="116" alt="image" src="https://github.com/user-attachments/assets/11985632-c8f1-4b3c-82b1-750b87c96371" />

Pilihan 3, melihat player terdepan:
<img width="302" height="118" alt="image" src="https://github.com/user-attachments/assets/7603e89f-0810-40fa-a5a1-43ec86f1bb6d" />

Pilihan 4, melihat antrean:
<img width="314" height="122" alt="image" src="https://github.com/user-attachments/assets/0dc4cd8f-16e7-4d43-98c2-e6b237535e5f" />

Pilihan 5, keluar prgram:
<img width="280" height="107" alt="image" src="https://github.com/user-attachments/assets/c05dd6c3-0a0d-4157-8383-2a1695941232" />


Video:


