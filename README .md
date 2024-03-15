# Running Tracker

url: http://carleano-ravelza-runningtracker.pbp.cs.ui.ac.id/

## Tugas 4
## Jawaban Soal

### Soal 1

[1] Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Kelebihannya adalah UserCreationForm akan memudahkan kita untuk membuat formulir untuk menambahkan user tanpa harus membuat form untuk register dan login user dari awal. Selain itu UserCreationForm juga sudah terintegrasi dengan sistem autentikasi Django. Kekurangannya adalah keterbatasannya, karena kita hanya dapat menggunakan fungsi yang disediakan oleh Django.
### Soal 2

[2] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah pengidentifikasian user untuk menentukan apakah user yang ingin masuk merupakan user yang otentik (asli) atau bukan. Sementara, otorisasi adalah pengecekan akses yang didasarkan pada identitas user, sehingga untuk setiap macam fitur, juga terdapat beberapa macam role yang boleh masuk.
### Soal 3

[4] Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies merupakan data kecil yang disimpan di dalam komputer pengguna dan dikirim dari web, sehingga jika suatu saat user mengakses web tersebut kembali, browser akan mengirimkan data cookies ke website itu. Karena sifat stateless dari HTTP, cookies seringkali digunakan untuk melakukan pengidentifikasian user (contohnya untuk menentukan apakah user yang login merupakan user yang sama yang login tadi).

Cara Django menggunakan cookies pertama-tama adalah Django membuat data session dari user yang disimpan dalam cookies dan disimpan dalam server. Kemudian data tersebut dikirimkan ke browser untuk nantinya disimpan berdasarkan pengaturan kedaluarsa yang diberikan oleh developer. Jika suatu saat user mengakses website itu kembali dengan browser yang sama, selama cookies tersebut masih aktif, cookies akan dikirim ke website agar website dapat mengenali user yang mengunjungi web tersebut kembali.
### Soal 4

[4] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Pada umumnya, fitur yang memudahkan user untuk melakukan autentikasi dan otorisasi membuat website semakin rentan. Tidak terkecuali cookies. Karena cookies dapat menyimpan data dan akan dikirimkan kembali ke server, hacker bisa saja mengubah data cookies tersebut demi kepentingan pribadi (seperti berpura-pura menjadi user lain). Terlebih cookies disimpan di sisi pengguna, jika kita tidak memfilter dan mengenkripsi dengan baik data pada cookies, hacker akan dapat dengan mudah meretas keamanan dari web yang kita miliki. Seperti contohnya dengan cookies poisoning.
### Soal 5

[5] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Checklist:

[ ] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Untuk mengimplementasi fungsi autentikasi dan otorisasi, kita dapat menambahkannya pada views.py. Untuk fitur registrasi, kita dapat memanfaatkan UserCreationForm milik django agar kita dapat dengan mudah membuat form pendaftaran user. Dengan UserCreationForm juga kita dapat langsung mengintegrasikan antara fitur registrasi dengan autentikasi dan otorisasi milik Django. Untuk method yang diterima, kita harus memilih POST agar data dari user tidak dikirim melalui url.

Untuk fitur login, kita juga dapat membuat form login sendiri. Pertama-tama, kita akan membuat file html sederhana agar user dapat memasukkan data-data login. Kemudian sama seperti ketika kita membuat fungsi register, kita akan merender laman login.html jika user melakukan request GET, sementara kita akan menerima data dari form jika user melakukan request POST. Setelah itu kita dapat memanggil fungsi login milik Django.

Setelah itu jangan lupa untuk menambahkan routing pada setiap fungsi.

Fitur logout dapat dilakukan dengan menjalankan fungsi logout. Untuk langkah ini, kita dapat membuat fungsi views baru yang menjalankan fungsi logout tersebut.

[ ] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model buku yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Form yang tadi kita telah buat akan terdapat pada salah satu route yang telah kita buat. Untuk fungsi register, form pendaftaran akan muncul secara otomatis dan kita tinggal mengisi data-data sesuai yang kita ingin berikan.

[ ] Menghubungkan model Item dengan User.

Untuk menghubungkan model Item dengan User, kita dapat menambahkan foreign key dari user pada table item. dengan menggunakan object ForeignKey.

[ ] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Untuk menampilkan nama user yang sedang login, kita dapat mengaksesnya pada request.user.username. Sementara untuk cokies seperti last login kita dapat memanggil request.COOKIES dan memasukkan key 'last_login'.

## Tugas 5
## Jawaban Soal

### Soal 1

[1] Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

#### Selektor Tunggal (elementname):
Manfaat: memilih semua elemen yang sesuai namanya.
Waktu yang tepat untuk digunakan: menerapkan style tertentu pada semua elemen di kode

#### Selektor Kelas (.classname):
Manfaat: memilih semua elemen yang memiliki value dari atribut class yang sama.
Waktu yang tepat untuk digunakan: saat ingin menerapkan style yang sama pada beberapa elemen yang sama, tetapi tidak semua elemen.

#### Selektor ID (#idname):
Manfaat: memilih elemen tertentu secara spesifik. Selektor ini memilih elemen dengan ID yang cocok.
Waktu yang tepat untuk digunakan: saat ingin menerapkan style tertentu pada suatu elemen spesifik.

##### Selektor Universal (*):
Manfaat: memilih semua elemen dalam dokumen.
Waktu yang tepat untuk digunakan:saat ingin menerapkan base style pada kode

#### Selektor Grup (,):
Manfaat: membuat beberapa selektor menjadi satu aturan CSS
Waktu yang tepat untuk digunakan: menerapkan style yang sama pada elemen yang berbeda

### Soal 2

[2] Jelaskan HTML5 Tag yang kamu ketahui.

#### header: 
Digunakan untuk menentukan bagian atas dari sebuah halaman web.

#### section: 
digunakan unuk mengelompokkan section yang berhubungan.

#### footer: 
Menandakan bagian paling bawah dari sebuah halaman web. 

#### div:
digunakan untuk menegelompokkan konten dalam dokumen HTML. 

#### main: 
Menunjukkan konten yang utama dari web.

#### body:
menunjukkan isi konten web

### Soal 3

[3] Jelaskan perbedaan antara margin dan padding

Margin menentukan ruang yang berada di luar batas elemen, seperti mengontrol jarak antara elemen dengan elemen lainnya.Sementara itu, padding menentukan ruang yang berapa di antara batas elemen dan konten yang ada di dalamnya, seperti mengatur jarak antara konten dengan batas elemen.

### Soal 4

[4] Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

komponen tailwind lebih spesifik, tidak siap pakai seperti bootstrap. Bootstrap cocok untuk prototyping. bootstrap berdasarkan functionality, sedangkan tailwind berdasarkan karakterisitik dan jauh lebih bebas. Bootstrap lebih cocok untuk proyek yang berdasarkan prototyping dan menginginkan style yang konsisten, sedangkan tailwind cocok digunakan untuk design yang lebih spesifik dan bebas. 


