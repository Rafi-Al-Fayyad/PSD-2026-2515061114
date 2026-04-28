Tugas Akhir Percobaan 1

Judul Program : Daftar Absensi Siswa

Program ini digunakan untuk mencatat absensi siswa di sekolah dengan menggunakan list 1 dimensi pada Python. Saat program dijalankan, pengguna terlebih dahulu diminta memasukkan jumlah siswa, lalu program akan menyiapkan tempat penyimpanan data sesuai jumlah tersebut. Setelah itu, pengguna dapat memilih beberapa menu seperti melihat address array, melihat address setiap index, mengisi data absensi siswa, melihat daftar absensi, dan keluar dari program. Menu address digunakan untuk mengetahui letak penyimpanan data di memori, baik untuk list secara keseluruhan maupun setiap elemennya. Pada bagian input data, pengguna memasukkan nama siswa yang hadir satu per satu dan program akan menolak jika ada input yang kosong. Setelah semua data diisi, daftar absensi dapat ditampilkan sehingga pengguna bisa melihat nama siswa yang sudah tercatat atau data yang masih belum diisi.

Source Code :
<img width="914" height="2812" alt="program absen jd1" src="https://github.com/user-attachments/assets/c8429a11-6690-4252-b41b-9ecaa4d114d8" />

1. Mendefinisikan fungsi menu program.
2. Mencetak judul sistem absensi sekolah ke layar.
3. Mencetak opsi pertama menu untuk menampilkan address array.
4. Mencetak opsi kedua menu untuk menampilkan address dari semua index array.
5. Mencetak opsi ketiga menu untuk memasukkan data absensi siswa.
6. Mencetak opsi keempat menu untuk menampilkan daftar absensi.
7. Mencetak opsi kelima menu untuk keluar dari program.
8. 
9. Mendefinisikan fungsi utama program tempat seluruh logika inti berjalan.
10. Meminta user memasukkan jumlah siswa yang akan diinput ke dalam absensi.
11. Membuat list 1 dimensi bernama absen dengan jumlah elemen sesuai input user.
12. Membuat variabel running untuk menjaga agar program tetap berjalan.
13.     
14. Memulai perulangan utama selama variabel running bernilai True.
15. Memanggil fungsi menu yang sudah didefinisikan di awal untuk tampil ke layar.
16. 
17. Mencoba menjalankan input pilihan.
18. Mengambil input pilihan menu dari user dan mengubahnya menjadi bilangan bulat (integer).
19. Menangkap error jika user memasukkan sesuatu yang bukan angka.
20. Menampilkan pesan error.
21. Mengulang perulangan dari awal menu jika terjadi error input.
22. 
23. Mengecek jika user memilih menu nomor 1.
24. Menampilkan address atau alamat memori dari array absensi secara keseluruhan menggunakan fungsi id().
25. 
26. Mengecek jika user memilih menu nomor 2.
27. Mencetak judul bagian address dari setiap index array.
28. Melakukan perulangan sebanyak jumlah siswa.
29. Menampilkan address dari setiap elemen list absen berdasarkan index masing-masing.
30. 
31. Mengecek jika user memilih menu nomor 3.
32. Mencetak judul bagian input data absensi siswa.
33. Melakukan perulangan untuk menginput nama siswa sesuai jumlah siswa.
34. Melakukan perulangan tanpa henti sampai user memasukkan nama yang valid.
35. Meminta input nama siswa sesuai urutan absensi.
36. 
37. Melakukan pengecekan apakah input kosong atau hanya berisi spasi.
38. Jika kosong, menampilkan pesan bahwa nama tidak boleh kosong.
39. Jika input valid, program masuk ke bagian else.
40. Menyimpan nama siswa ke dalam list absen pada index yang sesuai.
41. Keluar dari perulangan while True dan lanjut ke siswa berikutnya.
42. 
43. Menampilkan pesan bahwa data absensi berhasil disimpan.
44. 
45. Mengecek jika user memilih menu nomor 4.
46. Mencetak judul daftar absensi siswa.
47. Melakukan perulangan untuk menampilkan semua data absensi.
48. Mengecek apakah data pada index tersebut masih kosong.
49. Jika kosong, menampilkan status bahwa absensi belum diisi.
50. Jika data sudah ada, program masuk ke bagian else.
51. Menampilkan nama siswa yang sudah tersimpan pada list absensi.
52. 
53. Mengecek jika user memilih menu nomor 5.
54. Mengubah running menjadi False agar perulangan program berhenti.
55. Menampilkan pesan bahwa program selesai.
56. 
57. Jika user memasukkan angka yang tidak ada di menu.
58. Menampilkan pesan bahwa pilihan tidak valid.
59. 
60.
61. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi langsung.
62. Memanggil fungsi utama untuk menjalankan seluruh program.

Output masukkan jumlah siswa :
<img width="296" height="23" alt="Screenshot 2026-04-28 202328" src="https://github.com/user-attachments/assets/00ebe3a5-4a84-4f22-a89e-591ac5147ba8" />

Setelah diinputkan jumlah siswa :
<img width="521" height="176" alt="Screenshot 2026-04-28 202345" src="https://github.com/user-attachments/assets/da0fdae6-3c5a-4bad-ac2c-afad64296193" />

Output menu 1 :
<img width="426" height="82" alt="image" src="https://github.com/user-attachments/assets/54a0c675-2d6f-49bc-b277-848e0d9281de" />


Output menu 2 :
<img width="399" height="159" alt="image" src="https://github.com/user-attachments/assets/cf804865-d8ac-48f7-ad86-069cc45e95eb" />

Menu 3 setelah diinputkan nama :
<img width="381" height="166" alt="Screenshot 2026-04-28 202431" src="https://github.com/user-attachments/assets/87201a01-5474-4433-b5a1-998098668457" />

Output menu 4 :
<img width="272" height="108" alt="Screenshot 2026-04-28 202525" src="https://github.com/user-attachments/assets/7bdc8955-9544-4096-b155-2282b3a33b75" />

Output menu 5 :
<img width="186" height="35" alt="image" src="https://github.com/user-attachments/assets/8b85d7ab-52ea-4acc-a233-73e62925da5d" />

Video : https://youtu.be/zWs-AIUCZ08



