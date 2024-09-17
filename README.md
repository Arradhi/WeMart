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

========================================================================

Tugas 3 PBP

1. 
Data delivery sangat diperlukan dalam platform sebagai media komunikasi antara client dengan server maupun komunikasi internal yang terjadi di dalam proyek kita. Jika proyek kita tidak memiliki data delivery, akan ada potensi dimana request client tidak bisa terpenuhi Sebagian atau seutuhnya. hali ini juga berlaku sebaliknya dimana jika client tidak bisa mengirim data, maka proyek berpotensi tidak bisa memproses kebutuhan client dikarenakan kurangnya informasi.

2. 
antara XML dan JSON, keduanya memiliki kelebihan dan kekurangan masing-masing sehingga kita dapat menggunakan keduanya sesuai dengan kebutuhan kita.
XML lebih cocok digunakan ketimbang JSON disaat kita berurusan dengan file-file yang kompleks dan banyak memiliki nested elements. hal ini memiliki variabel yang bisa dideklarasikan secara bebas dan independen serta struktur XML yang mendukung hirarki. Contoh aplikasi nyatanya seperti file yang berisikan kumpulan putusan hukum atau pasal negara.
Sementara JSON lebih cocok digunakan saat kita berurusan dengan web atau aplikasi sehari-hari khususnya untuk mobile platform yang memiliki keterbatasan resource. JSON terkenal ringan dan strukturnya tersusun atas key dan value sehingga mudah diolah oleh komputer. ketimbang XML. JSON merupakan pilihan tepat yang dapat digunakan untuk menyimpan data user pada website kecil dengan keterbatasan hardware yang dimiliki sehingga hal inilah yang membuat JSON lebih populer 

3. 
method is_valid() yang kita definisikan pada method creat_product_entry di views.py berfungsi untuk melakukan validasi terhadap input yang akan diberikan pada form sesuai dengan aturan yang telah kita definisikan. Tanpa validasi ini, form bisa menerima data yang tidak valid atau berbahaya, yang dapat menyebabkan error atau kerentanan keamanan di aplikasi.

4. 
CSRF_token merupakan sebuah token unik yang ditambahkan sebagai bagian dalam request kepada suatu website. Token ini mencegah serangan CSRF (Cross-Site Request Forgery) dimana penyerang bisa mengeksploitasi sesi pengguna yang sedang aktif dan mengirimkan request yang tidak terotorisasi oleh pengguna aslinya pada website. Jika kita tidak menggunakan csrf_token, system tidak bisa membedakan mana request yang datang dari pengguna asli atau penyerang sehingga kedua request tersebut akan diakui oleh system. Sementara dengan adanya CSRF_token, dalam membuat request penyerang perlu menyertakan token yang sama dalam membuat request palsunya dimana hal ini hamper tidak mungkin untuk ditebak.

5.
Pertama-tama kita perlu membuat skeleton sebagai kerangka views dengan nama base.html. Dengan adanya skeleton kita dapat menjaga konsistensi pada desain web kita. selanjutnya kita perlu menambahkan BASE_DIR / 'templates' pada list DIRS agar base.html yang kita buat dapat dikenali.

berikutnya kita perlu menambahkan {% extends 'base.html' %} pada main.html kita agar template html mengikuti kerangka yang sudah dibuat pada base.html
selanjutnya kita akan mengubah primary key dari integer menjadi UUID pada models Product yang telah kita buat untuk mencegah celah keamanan serangan IDOR.

Setelah migrasi models, kita dapat mulai membuat form untuk data delivery. pertama buat form.py pada direktori main. selanjutnya import modul yang diperlukan dan buat objek formnya. saat form dikirim, data akan disimpan sebagai object yang kita deklarasikan pada form tersebut (dalam kasus ini merupakan object Products yang ada pada models).

Selanjutnya kita akan mengimport object form tadi ke views.py. lalu kita akan membuat fungsi untuk menambahkan data product entry secara otomatis dan akan mengembalikan tampilan ke main.html Ketika data di submit. fungsi ini juga menghandle render terhadap tampilan html disaat user akan mengisi form. 

Setelah itu, kita akan menambahkan object Product.objects.all() yang akan di assign ke variable product_entries di fungsi show_main pada main. setelah itu ita akan menambahkan product_entries tersebu kedalam context pada fungsi show_main. hal ini bertujuan agar semua object products pada database dapat diambil.

Selanjutnya kita akan mengimport fungsi tersebut ke urls.py yang ada di main dan menambahkannya ke path agar request form yang dating dapat diarahkan ke create_product_entries. Setleah itu kita akan membuat html pada main/templates yang Bernama create_product_entry.html. file ini berfungi untuk handle tampilan html disaat user akan mengisi form. html ini terhubung dengan forms.py sehingga kolom-kolomnya dapat diterapkan secara otomatis. Selanjutnya kita tambahkan line code yang akan memberikan tampilan berupa tbel mengenai objek-objek (dalam hal ini Products) yang ditambahkan melalui form data delivery pada tampilan main.html. 

Berikutnya kita akan membuat fungsi untuk mengembalikan data-data yang ada di dalam object Products yang ditambahkan melalui form dalam bentuk JSON dan XML. Pertama import modul yang diperlukan seperti HttpRespone dan serializers. Serializers berfungsi untuk menerjemahkan objek model menjadi format lain seperti XML atau JSON. Lalu kita cukup membuat sebuah fungsi yang menerima parameter request dan menampilkan semua object yang ada pada class Products. setelah itu kita return HttpResponse berisikan data yang di serialize menjadi XML atau JSON. hal yang sama juga berlaku pada fungsi yang kita custom untuk lebih spesifik seperti show by id. dalam fungsi ini kita memfilter data objek secara spesifik sesuai dengan atribut yang kita inginkan. 

lalu tak lupa kita import fungsi-fungsi tersebut kedalam urls.py dan juga menambahkan path yang mengarah ke masing-masing fungsi. dengan begitu kita dapat mengakses XML atau JSON berisikan data-data objek Products melalui peramban web.

6. 
show JSON
![Logo](https://i.imgur.com/tfEvKQx.png)

show XML
![Logo](https://i.imgur.com/CGoWXjF.png)

show JSON by ID
![Logo](https://i.imgur.com/vcdm4Hh.png)

show XML by ID
![Logo](https://i.imgur.com/MseC1mN.png)








