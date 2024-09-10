Muhammad Fadhlan Arradhi - 2306240061

url website : https://muhammad-fadhlan32-wemart.pbp.cs.ui.ac.id/

1. 
pertama-tama dalam membuat sebuah project Django baru, kita perlu membuat direktori baru dimana kita akan menyimpan hal-hal yang diperlukan dalam project kita. Selanjutnya kita perlu masuk kedalam virtual environment python, hal ini dilakukan dengan mengetik python -m venv env dilanjutkan dengan 
env\Scripts\activate, hal ini dilakukan agar requirements dan dependencies yang akan kita pakai dalam proyek terisolasi dan tidak bertabrakan dengan versi diluar virtual environments. 

Selanjutnya kita harus mendownload requirements dan dependencies yang kita perlukan dalam membangun project kita. untuk mempermudah langkah ini, kita bisa menuliskan nama-nama modul yang akan kita pakai pada txt file dan menjalankan pip install -r requirements.txt untuk mendownload semuanya sekaligus.

setelah semua requirements didownload, kita bisa memulai proyek dengan perintah 
django-admin startproject WeMart . dimana WeMart adalah nama sebuah project e-commerce yang saya buat. setelah itu, dalam direktori saya akan muncul beberapa file configuration Django yang dapat dimodifikasi sesuai kebutuhan. lalu saya menjalankan python manage.py runserver dan membuka http://localhost:8000 untuk mencoba apakah direktori tersebut sudah siap digunakan sebagai platform pengembangan website atau tidak. setelah berhasil saya ctrl + c dan deactivate server untuk bersiap melakukan pengembangan website.

saya mulai dari membuat aplikasi main pada proyek ini dengan menjalankan python manage.py startapp main
perintah ini akan membuat direktori main yang berisikan beberapa hal seperti views, urls dan lain-lain yang bisa dikonfigurasi sesuai kebutuhan. berikutnya saya menambahkan 'main' dalam INSTALLED_APPS pada settings.py didalam direktori WeMart yang terbentuk saat saya startproject sebelumnya. Hal ini dilakukan agar aplikasi main yang kita tambahkan tadi terdaftar dan terhubung dengan project kita.

berikutnya saya akan mengkonfigurasi urls.py pada direktori WeMart untuk diarahkan ke urls main nantinya. ini berfungsi untuk mengarahkan url awal menuju main agar karena kita akan mengkonfigurasi tampilan web disana. pertama tambahkan from django.urls import path, include lalu tambahkan  
path('', include('main.urls')), sehingga nantinya file ini akan merefer pada file urls yang ada di main.

Selanjutnya, saya akan membuat model dalam aplikasi main. pertama buat file dengan nama models.py     
disini saya mendefinisikan jenis-jenis field yang akan saya pakai untuk nantinya ditampilkan melalui html. pada model ini, saya memberi nama class dengan Products dan class ini memiliki 4 atribut diantaranya name, description, price sebagai atribut wajib dan saya menambahkan image sebagai atribut tambahan. setelah itu saya melakukan migrasi pada model saya agar django dapat mendeteksi perubahan pada model saya dengan perintah python manage.py makemigrations dilanjutkan dengan python manage.py migrate.

setelah itu, saya lanjut mengkonfigurasikan views.py file ini berfungsi untuk melakukan render pada hal-hal yang akan ditampilkan.
pada dictionary di file ini, string key disesuaikan dengan nama variable yang terdefinisi di models.py selanjutnya nama fungsi show_main(request) disesuaikan dengan nama fungsi yang dipanggil pada urls.py di aplikasi main serta parameter request ditujukan untuk menerima request dari urls.py tersebut. terakhir fungsi ini akan memberikan request render ke file html untuk di render sesuai dengan layout yang akan didefinisikan pada file htmlnya

setelah itu, saya lanjut membuat file html untuk mengatur layout tampilan pada website nanti.
pada code ini, saya mendefinisikan h1 sebagai header Utama berisikan nama toko dan juga identitas saya. Selanjutnya saya mendefinisikan h5 pada Harga dan deskripsi sebagai sub header dan p pada konten Harga dan deskripsi sebagai paragraph isi. terakhir saya menambahkan image untuk gambar dari produk yang akan dijual. nama didalam { } disesuaikan dengan yang telah didefinisikan pada models dan views

Setelah itu, saya akan mengkonfigurasi routing url pada aplikasi main. hal ini dilakukan agar tampilan yang telah dikonfigurasi di aplikasi main dapat diakses di web. pertama kita buat urls.py pada direktori main.
code ini berfungsi untuk mengarahkan tampilan menuju views.py yang ada dalam aplikasi main apabila urls.py pada main akan diakses. line code ini juga memberikan identitas pada app_name sebagai nama unik untuk menjadi key akses. 

terakhir, setelah proyek selesai dibuat, saya akan mengupload proyek saya ke pws agar websitenya dapat dilihat semua orang. pertama saya melakukan git init pada direktori proyek saya. kemudian saya membuat repo baru pada GitHub dan mengcopy link reponya. kemudian saya membuat branch baru dengan nama main menggunakan perintah git branch -M main. selanjutnya saya menghubungkan directory local saya dengan GitHub memlalui perintah git remote add origin <link-github-saya>. terakhir saya menambahkan .gitignore agar berkas-berkas yang tidak diperlukan dapa diabaikan oleh git. setelah itu saya melakukan git add, commit dan push untuk mengupload project saya ke GitHub

setelah project terupload di GitHub, saya dapat mengupload project saya menggunakan pws. pertama create new project dan sesuaikan nama di pws dengan nama project kita dan jangan lupa untuk menyimpan credentials yang diberikan. setelah itu tambahkan <username-sso>-<nama proyek>.pbp.cs.ui.ac.id di ALLOWED_HOSTS pada settings.py di project kita. lalu lakukan add, commit, push Kembali. setelah itu kita dapat menjalankan perintah yang terdapat di pws untuk mendeploy project kita dengan memasukan credentials yang tadi diberikan. dengan begitu project kita sudah dapat diakses oleh siapapun.

2. 
![Logo](https://i.imgur.com/F5Inpzo.png)

client melakukan request melalui urls.py yang ada di dalam proyek, setelah itu urls.py proyek meneruskan request tersebut ke urls.py yang ada pada main. Selanjutnya urls.py menerima request lalu memanggil view.py, pada view.py main.html dan models.py dipanggil untuk di render sesuai dengan request yang diberikan client berdasarkan code yang telah di definisikan. setelah request.py siap untuk ditampilkan, view.py mengirim http response ke client. 

3. 
git merupakan tools yang berfungsi sebagai version control system. dengan git, kita dapat melacak perubahan apa saja yang kita lakukan pada proyek kita. kita juga dapat mengembalikan proyek ke versi sebelumnya apabila erdapat asalah pada versi terbarunya. Selain itu, git juga memungkinkan kita untuk berkolaborasi dalam mengerjakan proyek. kita dapat melakukan perubahan pada device lokal masing-masing sebelum melakukan integrasi dengan menggabungkan perubahan yang telah dilakukan melalui git

4. 
Django merupakan salah satu framework yang terkenal dan sudah ramai dipakai dalam proyek pengembangan perangkat lunak. Selain itu, Django menggunakan Bahasa pemrograman python dimana python merupakan Bahasa pemrograman yang terkenal dan sangat ramah untuk pemula sehingga pemilihan Django sebagai framework pertama yang dipelajari bagi pemula adalah pilihan yang direkomendasikan. 

5. 
Object-Relational-Mapping merupakan metode yang digunakan Django untuk menghubungkan dan mengelola interaksi antar object pada python dan database yang dimiliki. dengan memetakan data yang ada di database ke object python, kita dapat membawa konsep object dan class dalam berurusan dengan database tanpa perlu berurusan dengan query seperti query sql secara langsung 


