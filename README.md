# Praktikum 7
Tugas Pemrograman Dasar Pertemuan Ke 12 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Tugas Praktikum
<ul>
  <li>Flowchart</li>
  <img src="https://github.com/aramli/labpy07/raw/main/img/20.png" width="750"/>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy07/raw/main/img/1.png" width="750"/>
  <img src="https://github.com/aramli/labpy07/raw/main/img/2.png" width="750"/>
  <img src="https://github.com/aramli/labpy07/raw/main/img/3.png" width="750"/>
  <li>Hasil Program</li>
    1. Lihat Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/14.png" width="750"/><br>
    2. Menambahkan Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/15.png" width="750"/><br>
    3. Mengubah Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/16.png" width="750"/><br>
    4. Menghapus Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/17.png" width="750"/><br>
    5. Mencari Data Mahasiswa<br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/18.png" width="750"/><br>
    6. Keluar Dari Program<br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/19.png" width="750"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy07/raw/main/img/4.png" width="850"/><br>
  1. Pertama-tama, Class Mahasiswa digunakan untuk merepresentasikan satu mahasiswa dengan atribut penting seperti NIM, nama, nilai tugas, UTS, dan UAS. Pada saat objek dibuat, constructor __init__ akan langsung menghitung nilai akhir berdasarkan bobot yang sudah ditentukan, yaitu 30% untuk tugas, 35% untuk UTS, dan 35% untuk UAS. Dengan cara ini, setiap objek mahasiswa otomatis memiliki nilai akhir tanpa perlu dihitung manual lagi. Selain itu, terdapat method khusus __str__ yang berfungsi untuk menampilkan data mahasiswa dalam format string yang rapi. Method ini akan dipanggil secara otomatis ketika objek dicetak menggunakan print(), sehingga informasi mahasiswa dapat ditampilkan dengan mudah dan terstruktur.

<br><br>
 <img src="https://github.com/aramli/labpy07/raw/main/img/5.png" width="850"/><br>
  2. Selanjutnya, Class DataMahasiswa bertugas sebagai pengelola kumpulan data mahasiswa. Di dalam constructor __init__, dibuat sebuah dictionary kosong bernama data_mahasiswa yang akan digunakan untuk menyimpan data mahasiswa. Key dari dictionary adalah NIM, sedangkan value adalah objek dari kelas Mahasiswa. Dengan struktur ini, data mahasiswa dapat diakses, ditambah, diubah, dihapus, atau dicari dengan mudah berdasarkan NIM. Kelas ini menjadi pusat logika program karena menyediakan berbagai method untuk melakukan operasi CRUD terhadap data mahasiswa.

<img src="https://github.com/aramli/labpy07/raw/main/img/6.png" width="850"/><br>
  3. Kemudian, Method lihat_data digunakan untuk menampilkan seluruh data mahasiswa dalam bentuk tabel. Pertama, program mencetak header tabel agar tampilan lebih rapi. Jika dictionary data_mahasiswa kosong, maka akan ditampilkan pesan bahwa tidak ada data mahasiswa. Namun jika ada data, program akan melakukan iterasi terhadap setiap item dalam dictionary. Setiap mahasiswa ditampilkan dengan nomor urut, NIM, nama, nilai tugas, UTS, UAS, dan nilai akhir. Pada versi yang sudah diperbaiki, atribut mahasiswa diakses menggunakan mhs.nama, mhs.tugas, dan seterusnya, karena mhs adalah objek, bukan dictionary.

<br><br>
<img src="https://github.com/aramli/labpy07/raw/main/img/7.png" width="850"/><br>
  4. Lalu, Method tambah_data berfungsi untuk menambahkan data mahasiswa baru. Program akan meminta input dari pengguna berupa NIM, nama, nilai tugas, UTS, dan UAS. Setelah data dimasukkan, dibuatlah objek Mahasiswa baru dengan data tersebut, lalu objek disimpan ke dalam dictionary data_mahasiswa menggunakan NIM sebagai key. Dengan cara ini, setiap mahasiswa baru langsung tersimpan dalam sistem dan dapat diakses kembali.
<br><br>

  <img src="https://github.com/aramli/labpy07/raw/main/img/8.png" width="750"/><br>
  5. Selanjutnya, Method ubah_data memungkinkan pengguna memperbarui data mahasiswa yang sudah ada. Program akan meminta NIM mahasiswa yang ingin diubah. Jika NIM ditemukan dalam dictionary, maka pengguna diminta memasukkan data baru berupa nama, nilai tugas, UTS, dan UAS. Data lama akan diganti dengan objek Mahasiswa baru yang berisi data terbaru. Jika NIM tidak ditemukan, program akan menampilkan pesan error agar pengguna memeriksa kembali NIM yang dimasukkan.
<br><br>

  <img src="https://github.com/aramli/labpy07/raw/main/img/9.png" width="850"/><br>
  6. Berikutnya, Method cari_data digunakan untuk mencari data mahasiswa berdasarkan NIM. Program akan meminta input NIM, lalu memeriksa apakah NIM tersebut ada dalam dictionary. Jika ditemukan, data mahasiswa akan ditampilkan dengan memanfaatkan method __str__ dari kelas Mahasiswa, sehingga informasi mahasiswa ditampilkan secara rapi. Jika tidak ditemukan, program akan menampilkan pesan bahwa data tidak ada.

<br><br>
  <img src="https://github.com/aramli/labpy07/raw/main/img/10.png" width="850"/><br>
  7. Kemudian, Method hapus_data berfungsi untuk menghapus data mahasiswa dari dictionary. Program akan meminta input NIM, lalu memeriksa apakah NIM tersebut ada dalam dictionary. Jika ada, data mahasiswa akan dihapus menggunakan perintah del. Jika tidak ditemukan, program akan menampilkan pesan bahwa data tidak ada. Dengan cara ini, pengguna dapat menghapus data mahasiswa yang tidak diperlukan lagi.

<br><br>
<img src="https://github.com/aramli/labpy07/raw/main/img/11.png" width="850"/><br>
  8. Lalu, Method cari_data digunakan untuk mencari data mahasiswa berdasarkan NIM. Program akan meminta input NIM, lalu memeriksa apakah NIM tersebut ada dalam dictionary. Jika ditemukan, data mahasiswa akan ditampilkan dengan memanfaatkan method __str__ dari kelas Mahasiswa, sehingga informasi mahasiswa ditampilkan secara rapi. Jika tidak ditemukan, program akan menampilkan pesan bahwa data tidak ada.

<br><br>
<img src="https://github.com/aramli/labpy07/raw/main/img/11.png" width="850"/><br>
  8. Lalu, Method main adalah menu utama program yang berjalan dalam loop. Program akan menampilkan pilihan kepada pengguna, yaitu lihat data, tambah data, ubah data, hapus data, cari data, atau keluar. Setiap pilihan akan memanggil method yang sesuai. Program akan terus berjalan hingga pengguna memilih opsi keluar. Dengan adanya menu ini, pengguna dapat berinteraksi langsung dengan sistem secara sederhana dan terstruktur.

<br><br>
<img src="https://github.com/aramli/labpy07/raw/main/img/11.png" width="850"/><br>
  8. Lalu, Pada bagian akhir, terdapat blok if __name__ == "__main__": yang memastikan program hanya dijalankan ketika file tersebut dieksekusi secara langsung. Di dalam blok ini, dibuat objek dari kelas DataMahasiswa dan dipanggil method main untuk memulai menu interaktif. Dengan struktur ini, program menjadi modular, terorganisir, dan mudah dikembangkan lebih lanjut.
<br><br>
</ul>
