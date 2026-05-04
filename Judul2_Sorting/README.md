Tugas Akhir Percobaan 2

Program Pengurutan Judul Buku Berdasarkan Abjad

Program ini digunakan untuk mengurutkan judul buku berdasarkan abjad (A–Z) menggunakan algoritma Bubble Sort. Pengguna diminta memasukkan jumlah judul buku, kemudian memasukkan setiap judul satu per satu. Data yang dimasukkan akan diproses dengan metode Bubble Sort, yaitu membandingkan dua judul yang berdekatan dan menukarnya jika urutannya tidak sesuai. Proses ini dilakukan berulang hingga semua judul tersusun rapi secara alfabet. Setelah proses selesai, program akan menampilkan daftar judul buku sebelum dan sesudah diurutkan.

<img width="1410" height="2116" alt="Program pengurutan buku jd2" src="https://github.com/user-attachments/assets/2c892760-693e-4b13-b02c-db22175c3789" />

1.	Mendefinisikan fungsi bernama tukar yang digunakan untuk menukar posisi dua elemen dalam array berdasarkan index.
2.	Menyimpan sementara nilai elemen pada index i ke dalam variabel temp agar tidak hilang saat proses penukaran.
3.	Mengisi posisi index i dengan nilai dari index j.
4.	Mengisi posisi index j dengan nilai yang sebelumnya disimpan di temp, sehingga kedua elemen berhasil ditukar.
5.	
6.	
7.	Mendefinisikan fungsi bubble_sort yang bertugas mengurutkan isi array menggunakan metode Bubble Sort.
8.	Melakukan perulangan luar sebanyak n - 1 kali, karena dalam Bubble Sort maksimal diperlukan n-1 tahap untuk memastikan semua data terurut.
9.	Melakukan perulangan dalam untuk membandingkan elemen yang bersebelahan dari awal hingga bagian yang belum terurut.
10.	Membandingkan dua elemen bertipe string dengan mengubah keduanya ke huruf kecil (lower()), agar pengurutan tidak terpengaruh huruf besar/kecil.
11.	Memanggil fungsi tukar untuk menukar posisi kedua elemen agar urutan menjadi benar.
12.	
13.	
14.	Mendefinisikan fungsi main sebagai fungsi utama yang mengatur alur program dari awal sampai akhir.
15.	Memulai blok try untuk mengantisipasi kesalahan saat user memasukkan jumlah buku.
16.	Meminta user memasukkan jumlah buku yang akan diinput, lalu mengubahnya menjadi tipe data integer.
17.	Menangkap error ValueError jika user memasukkan input selain angka.
18.	Menampilkan pesan bahwa input tidak valid agar user tahu kesalahannya.
19.	Menghentikan program menggunakan return jika terjadi kesalahan input.
20.	
21.	Membuat list kosong bernama arr yang akan digunakan untuk menyimpan judul-judul buku.
22.	
23.	Menampilkan pesan instruksi kepada user untuk mulai memasukkan judul buku.
24.	Melakukan perulangan sebanyak jumlah buku (n) agar semua judul bisa diinput.
25.	Meminta user memasukkan judul buku satu per satu sesuai urutan.
26.	Menambahkan setiap judul yang diinput ke dalam list arr menggunakan method append().
27.	
28.	Menampilkan isi list arr sebelum dilakukan proses pengurutan, agar bisa dibandingkan dengan hasil setelah sorting.
29.	
30.	Memanggil fungsi bubble_sort dengan parameter array dan jumlah data untuk mengurutkan judul buku.
31.	
32.	Menampilkan judul bahwa data berikut adalah hasil setelah diurutkan.
33.	Melakukan perulangan untuk menampilkan semua isi array yang sudah diurutkan.
34.	Menampilkan setiap judul buku satu per satu sesuai urutan alfabet.
35.	
36.	
37.	Baris standar Python yang memastikan bahwa kode di dalam main() hanya dijalankan jika file ini dijalankan langsung, bukan di-import.
38.	Memanggil fungsi main() untuk menjalankan seluruh program dari awal.


Output: 

1. Pengguna diminta memasukkan jumlah buku yang akan diurutkan.
<img width="358" height="72" alt="image" src="https://github.com/user-attachments/assets/d09cc5f3-e752-4e37-aab6-e332e1b2c840" />

2. Pengguna diminta memasukkan judul-judul buku.
<img width="367" height="127" alt="image" src="https://github.com/user-attachments/assets/5651fe0d-6a76-4e26-a282-7dd5614343eb" />

3. Setelah memasukkan judul buku akan ditampilkan sebelum diurutkan dan setelah diurutkan.
<img width="1240" height="311" alt="image" src="https://github.com/user-attachments/assets/79ad02dc-ed3b-414f-a7ed-77cfdbe76166" />




