Tugas Akhir Percobaan 5

Program Leaderboard Game

Program ini merupakan implementasi struktur data Binary Search Tree (BST) yang digunakan untuk menyimpan dan mengelola data skor pemain dalam sebuah game. Program memiliki fitur menambahkan skor pemain, menampilkan leaderboard dari skor tertinggi ke terendah, mencari skor tertinggi dan terendah, mencari pemain berdasarkan skor, serta menghapus data pemain.

<img width="1494" height="6932" alt="code ta 5 leaderboard game" src="https://github.com/user-attachments/assets/6fbdadd3-9311-4ca2-a197-fe912816d24c" />

1.	Mendefinisikan class Node yang digunakan untuk membuat node pada Binary Search Tree. 
2.	Mendefinisikan method __init__ sebagai constructor untuk class Node. 
3.	Menyimpan nilai skor pemain ke dalam atribut score. 
4.	Menyimpan nama pemain ke dalam atribut player. 
5.	Membuat child kiri (left) dengan nilai awal None. 
6.	Membuat child kanan (right) dengan nilai awal None. 
7.	 
8.	Mendefinisikan class GameLeaderboard untuk mengelola data leaderboard game menggunakan BST. 
9.	Mendefinisikan constructor __init__ pada class GameLeaderboard. 
10.	Membuat root BST dengan nilai awal None. 
11.	 
12.	Mendefinisikan fungsi insert_node() untuk menambahkan node baru ke BST. 
13.	Mengecek apakah root kosong. 
14.	Jika kosong, membuat node baru menggunakan Node(score, player). 
15.	
16.	Mengecek apakah skor baru lebih kecil dari skor root. 
17.	Jika benar, data dimasukkan ke subtree kiri secara rekursif. 
18.	Jika tidak, 
19.	data dimasukkan ke subtree kanan secara rekursif. 
20.	 
21.	Mengembalikan root setelah proses insert selesai. 
22.	 
23.	Mendefinisikan fungsi insert() untuk mempermudah pemanggilan insert node. 
24.	Memanggil fungsi insert_node() dan menyimpan hasilnya ke root. 
25.	 
26.	Mendefinisikan fungsi descending_order() untuk menampilkan leaderboard dari skor terbesar ke terkecil. 
27.	Mengecek apakah root tidak kosong. 
28.	Memanggil subtree kanan terlebih dahulu agar skor terbesar ditampilkan lebih dulu. 
29.	Menampilkan nama pemain dan skor pemain. 
30.	Memanggil subtree kiri setelah subtree kanan selesai. 
31.	 
32.	Mendefinisikan fungsi highest_score() untuk mencari skor tertinggi. 
33.	Membuat variabel current yang menunjuk ke root BST. 
34.	 
35.	Mengecek apakah leaderboard kosong. 
36.	Jika kosong, mengembalikan nilai None. 
37.	 
38.	Melakukan perulangan selama node kanan masih ada. 
39.	Menggeser current ke node kanan karena skor terbesar berada di kanan BST. 
40.	 
41.	Mengembalikan node dengan skor tertinggi. 
42.	 
43.	Mendefinisikan fungsi lowest_score() untuk mencari skor terendah. 
44.	Membuat variabel current yang menunjuk ke root BST. 
45.	 
46.	Mengecek apakah leaderboard kosong. 
47.	Jika kosong, mengembalikan nilai None. 
48.	 
49.	Melakukan perulangan selama node kiri masih ada. 
50.	Menggeser current ke node kiri karena skor terkecil berada di kiri BST. 
51.	 
52.	Mengembalikan node dengan skor terendah. 
53.	 
54.	Mendefinisikan fungsi search_score() untuk mencari pemain berdasarkan skor. 
55.	Mengecek apakah root kosong. 
56.	Jika kosong, mengembalikan None. 
57.	 
58.	Mengecek apakah skor yang dicari sama dengan skor root. 
59.	Jika sama, mengembalikan node tersebut. 
60.	 
61.	Mengecek apakah skor yang dicari lebih kecil dari root. 
62.	Jika benar, pencarian dilanjutkan ke subtree kiri secara rekursif. 
63.	 
64.	Jika tidak, 
65.	pencarian dilanjutkan ke subtree kanan secara rekursif. 
66.	 
67.	Mendefinisikan fungsi delete_node() untuk menghapus node pada BST. 
68.	Mengecek apakah root kosong. 
69.	Jika kosong, mengembalikan None. 
70.	 
71.	Mengecek apakah skor yang dihapus lebih kecil dari root. 
72.	Jika benar, penghapusan dilakukan pada subtree kiri. 
73.	 
74.	Mengecek apakah skor yang dihapus lebih besar dari root. 
75.	Jika benar, penghapusan dilakukan pada subtree kanan. 
76.	 
77.	Jika skor ditemukan, proses penghapusan node dilakukan. 
78.	Mengecek apakah node tidak memiliki child kiri maupun kanan. 
79.	Jika benar, node dihapus dengan mengembalikan None. 
80.	 
81.	Mengecek apakah node hanya memiliki child kanan. 
82.	Jika benar, node diganti dengan child kanan. 
83.	 
84.	Mengecek apakah node hanya memiliki child kiri. 
85.	Jika benar, node diganti dengan child kiri. 
86.	 
87.	Membuat variabel temp untuk mencari successor pada subtree kanan. 
88.	Melakukan perulangan selama child kiri masih ada. 
89.	Menggeser temp ke kiri untuk mencari node terkecil pada subtree kanan. 
90.	 
91.	Mengganti skor root dengan skor successor. 
92.	Mengganti nama pemain root dengan nama pemain successor. 
93.	 
94.	Menghapus node successor yang sudah dipindahkan. 
95.	
96.	Mengembalikan root setelah proses delete selesai. 
97.	
98.	Mendefinisikan fungsi delete() untuk mempermudah pemanggilan delete node. 
99.	Memanggil fungsi delete_node() dan menyimpan hasilnya ke root. 
100. 
101. 
102. Mendefinisikan fungsi main() sebagai fungsi utama program. 
103. Membuat objek game dari class GameLeaderboard. 
104. 
105. Memulai perulangan program menu utama menggunakan while True. 
106. Menampilkan judul program leaderboard game. 
107. Menampilkan menu tambah skor pemain. 
108. Menampilkan menu tampilkan leaderboard. 
109. Menampilkan menu lihat skor tertinggi. 
110. Menampilkan menu lihat skor terendah. 
111. Menampilkan menu cari pemain berdasarkan skor. 
112. Menampilkan menu hapus pemain. 
113. Menampilkan menu keluar program. 
114. 
115. Meminta pengguna memilih menu program. 
116.  
117. Mengecek apakah pengguna memilih menu 1. 
118. Meminta input nama pemain. 
119. Meminta input skor pemain. 
120. Memasukkan data pemain ke BST menggunakan fungsi insert(). 
121. Menampilkan pesan bahwa skor berhasil ditambahkan. 
122. 
123. Mengecek apakah pengguna memilih menu 2. 
124. Menampilkan judul leaderboard. 
125. Memanggil fungsi descending_order() untuk menampilkan ranking pemain. 
126. 
127. Mengecek apakah pengguna memilih menu 3. 
128. Memanggil fungsi highest_score() untuk mencari skor tertinggi. 
129. 
130. Mengecek apakah data skor tertinggi ditemukan. 
131. Menampilkan nama pemain dengan skor tertinggi. 
132. Jika leaderboard kosong,
133. menampilkan pesan bahwa data kosong. 
134. 
135. Mengecek apakah pengguna memilih menu 4. 
136. Memanggil fungsi lowest_score() untuk mencari skor terendah. 
137.  
138. Mengecek apakah data skor terendah ditemukan. 
139. Menampilkan nama pemain dengan skor terendah. 
140. Jika leaderboard kosong, 
141. menampilkan pesan bahwa data kosong. 
142. 
143. Mengecek apakah pengguna memilih menu 5. 
144. Meminta input skor yang ingin dicari. 
145. Memanggil fungsi search_score() untuk mencari pemain berdasarkan skor. 
146. 
147. Mengecek apakah data ditemukan. 
148. Menampilkan nama pemain jika data ditemukan. 
149. Jika data tidak ditemukan,
150. menampilkan pesan gagal. 
151. 
152. Mengecek apakah pengguna memilih menu 6. 
153. Meminta input skor yang ingin dihapus. 
154. Memanggil fungsi delete() untuk menghapus data pemain. 
155. Menampilkan pesan bahwa data berhasil dihapus. 
156. 
157. Mengecek apakah pengguna memilih menu 7. 
158. Menampilkan pesan bahwa program selesai dijalankan. 
159. Menghentikan perulangan menggunakan break. 
160.
161. Jika pilihan menu tidak tersedia, 
162. menampilkan pesan error. 
163. 
164. 
165. Mengecek apakah file dijalankan sebagai program utama. 
166. Memanggil fungsi main() untuk menjalankan program.

Output: <img width="419" height="253" alt="image" src="https://github.com/user-attachments/assets/2d9189ae-f681-4222-b395-c3c2561635a0" />

Pilihan 1, memasukkan nama dan skor pemain: <img width="404" height="327" alt="image" src="https://github.com/user-attachments/assets/2db0f950-1569-4d4e-b09b-4e8275d10ee9" />

Pilihan 2, menampilkan leadaerboard: <img width="404" height="385" alt="image" src="https://github.com/user-attachments/assets/6ebf2e13-c80a-4735-947a-6c81c9d71c44" />

Pilihan 3, melihat skor tertinggi: <img width="396" height="287" alt="image" src="https://github.com/user-attachments/assets/d89a4332-2c77-4797-817c-7dcffb953869" />

Pilihan 4, melihat skor terendah: <img width="401" height="283" alt="image" src="https://github.com/user-attachments/assets/9657aba6-edf8-4059-8f58-941309ad14e1" />

Pilihan 5, mencari pemain berdasarkan skor: <img width="404" height="312" alt="image" src="https://github.com/user-attachments/assets/7245b4c8-dd3d-4972-99de-ca865031fde5" />

Pilihan 6, menghapus skor: <img width="443" height="679" alt="image" src="https://github.com/user-attachments/assets/de2b424a-4c28-4579-825c-3cbe6c8afad4" />

Pilihan 7, berhenti: <img width="429" height="271" alt="image" src="https://github.com/user-attachments/assets/5c8d3418-5857-4be6-be65-3d792ea9b208" />







