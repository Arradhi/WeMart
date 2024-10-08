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

Berikutnya kita akan membuat fungsi untuk mengembalikan data-data yang ada di dalam object Products yang ditambahkan melalui form dalam bentuk JSON dan XML. Pertama import modul yang diperlukan seperti HttpRespone dan serializers. Serializers berfungsi untuk menerjemahkan objek model menjadi format lain seperti XML atau JSON. Lalu kita cukup membuat sebuah fungsi yang menerima parameter request dan menampilkan semua object yang ada pada class Products. setelah itu kita return HttpResponse berisikan data yang di serialize menjadi XML atau JSON. hal yang sama juga berlaku pada fungsi yang kita custom untuk lebih spesifik seperti show by id. dalam fungsi ini kita bisa memfilter data objek secara spesifik sesuai dengan atribut yang kita inginkan. 

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

========================================================================

Tugas 4 PBP

1. 
Perbedaan Utama antara HTTPResponseRedirect() dan redirect() terletak pada parameter fungsiya.  HTTPResponseRedirect() menerima parameter berupa URL ecara eksplisit yang nantinya akan memberi respon pengalihan. Sementara redirect() menerima parameter berupa instance name atau function name yang nantinya akan secara otomatis memberikan respon pengalihan ke instance atau fungsi yang diberikan.

2. 
Kita perlu melakukan import models User yang telah diimplementasikan Django pada Models proyek kita. setelah itu kita definisikan user dalam model kita menggunakanan foreign keydengan syntax :  user = models.ForeignKey(User, on_delete=models.CASCADE) dengan foreign key, kita dapat menghubungkan produk-produk yang dibuat terhadap user unik yang sedang terlogin sehingga tiap user dapat memiliki data produk yang berbeda-beda

3. 
Authenication merupakan proses untuk melakukan verifikasi identitas pengguna. proses ini biasanya meminta pengguna utuk memasukan identitas seperti nama dan password lalu dicek kesesuaiannya pada database. kita dapat mengimplementasikan hal ini pada Django dengan
django.contrib.auth. kita dapat membuat sebuah fungsi login dan meletakan @login_required sebagai batasan login sebelum mengakses website.

Disisi lain, Authorization merupakan proses untuk memberikan atau membatasi akses pengguna pada sistem sesuai dengan identitas atau role yang mereka miliki. kita dapat menerapkan hal iinidengan Permission yang disediakan oleh django.contrib.auth.models. kita juga dapat menggunakan @permission_required pada fungsi yang dibatasai berdasarkan role yang sudah didefinisikan

4.
Django mengingat user yang sedang login dengan menggunakan holding state. hal ini biasanya diterapkan menggunakan session dan cookie. cookie merupakan storage kecil berukuran 4kb yang ada pada client. kita bisa saja menyimpan informasi langsung pada cookie tapi hal tersebut berpotensi menyebabkan hal-hal yang tidak diinginkan dari segi keamanan. Maka dari tu, Kita dapat menggunakan session dimana session ini memiliki session ID yang unik sehingga session ID inilah yang disimpan pada cookie. nantinya session ID ini akan dipetakan pada suatu struktur data di proyek kita untuk mendeteksi informasi klien yang    sedang login. Selain untuk melakukan holding state, Cookies biasanya digunakan untuk menyimpan preferensi pengguna serta melacak behaviour dan activity dari pengguna. Data yang ada pada Cookies bisa saja diretas melalui koneksi mencurigakan sehingga Cookies tidak sepenuhnya aman. maka dari itu lebih baik kita tidak menyimpan identitas user yang login dalam cookies secara eksplisit.

5. 
Pertama kita akan membuat form registrasi pada views.py menggunakan UserCreationForm agar pengguna dapat membuat akun. Selanjutnya kita membuat fungsi register yang menerima request dan form ini akan membuat object UserCrationForm yang nanti akan membuat user berdasarkan input data-datanya. prinsip kerja dari fungsi ini mirip dengan fungsi create_product_entry yang sama-sama menggunakan form. Selanjutnya kita buat tampilan HTML untuk halaman register pada main template. Tak lupa juga kita mengatur url pada urls.py dengan mengimport fungsi register dan menambahkannya pada urlpatterns.

Berikutnya kita akan membuat fungsi untuk login pada views.py kita perlu import authenticate, login, dan AuthenticationForm untuk membuat fungsi login. fungsi login_user menerima paramere request dan dia akan membuat object AuthenticationForm yang menerima data-data yang akan divalidasi. jika data-datanya sesuai engan yang ada di database, maka user akan masuk ke halaman main. selanjutnya kita definisikan tampilan HTML untuk login page pada main template dan menambahkan fungsi login_user pada urls.py


Setelah itu, kita akan membuat fungsi logout pada views,py dengan melakukan import logout. fungsi logout_user akan menerima request dan request tersebut akan diproses sehingga user terlogout dan di redirect ke login page. Tak lupa kita tambahkan fungsi ini pada urls.py pada aplikasi main

Selanjutnya, setelah kita selesai membuat fungsi-fungsi di views.py kita akan merestriksi akses show_main apabila user belum terlogin dengan mengimport login_required dan menambahkan decorator @login_required(login_url='/login') pada fungsi show_main. Lalu kita akan menggunakan Cookies untuk menerapkan holding state. kita akan mengimport datetime, HttpResponeRedirect dan reverse diamna kita akan menerapkan hal ini pada fungsi login_user jika form valid maka kita akan melakukan request dengan nama "last_login"untuk set cookie berisikan datetime. lalu kita akan menambahkan  request.COOKIES['last_login'] pada show_main dengan key :last_login" agar informasi ini dapat dilihat di halaman web. setelah itu kita juga akan mengkonfigurasi fungsi logout dengan mendelete cookies apabila user logout. kita juga akan memperlihatkan cookies last login melalui main.html yang akan mengambil context pada views.py

Berikutnya kita akan membuat tiap user memiliki data product_entry yang masing-masing unik. Kita perlu melakukan import models User yang telah diimplementasikan Django pada Models proyek kita. setelah itu kita definisikan user dalam model kita menggunakanan foreign keydengan syntax :  user = models.ForeignKey(User, on_delete=models.CASCADE) dengan foreign key, kita dapat menghubungkan produk-produk yang dibuat terhadap user unik yang sedang terlogin sehingga tiap user dapat memiliki data produk yang berbeda-beda. lalu kita akan mengubah create_product_entry pada views.py dengan mengubah mood_entry = form.save(commit=False) dan menambahkan request.user agar Django tidak langsung menyimpan data pada form ke atabase sehingga kita bisa mengarahkan form tersebut ke user yang sedang login melalui request.user. kita juga akan mengubah product_entries pada show_main dari yang tadinya all menjadi  product_entries = Products.objects.filter(user=request.user) sesuai engan user yang sedang login sehingga data yang ditampilkan merupakan data dari user yang sedang login saja. Setelah itu saya akan menambahkan "user_name" pada context dengan value request.user.username sehingga saya dapat menampilkan nama user yangs edang login pada main.html 

Terakhir kita akan membuat satu akun yang akan menjadi default value pada saat kita melakukan migrasi. setelah akun dibuat, kita akan melakukan migrasi dengan  python manage.py makemigrations dan akan ada opsi dimana kita akan mengetik 1 sebanyak dua kali untuk migrasi. setelah selesai kita jalankan python manage.py migrate untuk migrasi modelnya. lalu untuk best practice, kita akan mengubah DEBUG pada settings.py dengan meningmpor OS lalu mengubahnya menjadi PRODUCTION = os.getenv("PRODUCTION", False) | DEBUG = not PRODUCTION sehingga pada saat website error, client tidak dapat melihat debug code dari websitenya. Dengan begitu website kita sekarang dapat membuat beragam user dengan beragam jenis produk berbeda. pada tugas ini saya akan membuat 2 user dengan 3 produk berbeda. dengan melakukan register sebanyak 2 kali, lalu login pada masing-masing akun dan menambahkan 3 produk berbeda pada masing-masing akun.

========================================================================

Tugas 5 PBP


1.
Priorita CSS Selectoradalah sebagai berikut:
- Inline Style
- ID Selector
- Class Selectors
- Element Selector

Jika ada dua selector dengan tingkat prioritas yang sama, yang terakhir dalam urutan di file CSS akan diterapkan.

2. 
Responsive design penting untuk diterapkan karena tiap penggua nantina akan mengakses web melalui perangkat dengan ukuran layar yang berbeda-beda. Dengan menerapkan konsep responsive design, pengalaman yang didapat tetap optimal pada masing-masing device pengguna tanpa perlu membuat versi yang berbeda-beda

cotoh web dengan responsive design:
- Youtube.com

contoh web tanpa responsive design:
http://www.arngren.net/


3.
Margin : Ruang di luar border dari elemen. Margin mengatur jarak antara elemen yang satu dengan elemen lainnya.

Border : Garis yang mengelilingi padding dan konten elemen. Border menambah visual seperti garis di sekitar elemen, dan bisa diatur dengan berbagai gaya, warna, dan ketebalan.

Padding : Ruang di dalam border, antara konten elemen dan border itu sendiri. Padding mengatur jarak antara isi konten dan batas elemen.

contoh implementasi : 
div {
  margin: 20px;       
  border: 2px solid black;
  padding: 10px;    
}

ilustrasi :

![Logo](https://i.imgur.com/XvbUdSr.png)

4.
Flexbox
Flexbox adalah sistem layout CSS yang dirancang untuk membuat tata letak yang fleksibel dan responsif. Flexbox bekerja dengan elemen satu dimensi, yang berarti bahwa elemen-elemen tersebut bisa diatur dalam satu arah, baik secara horizontal (row) atau secara vertikal (column). Flexbox sangat berguna untuk mengatur elemen dalam sebuah kontainer dan memungkinkan elemen-elemen tersebut menyesuaikan diri sesuai ukuran kontainer yang berubah-ubah.

Kegunaan Flexbox:
- Alignment: Mengatur alignment elemen dengan mudah menggunakan properti seperti justify-    content (untuk alignment horizontal) dan align-items (untuk alignment vertikal).

- Flexible Widths: Elemen bisa otomatis menyesuaikan lebarnya sesuai ruang yang tersedia di kontainer.

- Order: Mengubah urutan tampilan elemen tanpa mengubah urutan di HTML menggunakan properti order.


Gridbox
CSS Grid adalah sistem layout dua dimensi yang memungkinkan kita untuk mengatur elemen dalam bentuk baris dan kolom. Ini lebih fleksibel dan kuat untuk membuat layout kompleks dibandingkan Flexbox karena bekerja di dua dimensi.


Kegunaan Grid Layout:
- Membuat Layout yang Kompleks: Grid memungkinkan pengaturan kolom dan baris secara bersamaan, sehingga cocok untuk layout seperti galeri foto atau dashboard.

- Mengontrol Ukuran Kolom dan Baris: Dengan grid-template-columns dan grid-template-rows, kita bisa menentukan lebar kolom dan tinggi baris secara spesifik.

- Menyusun Elemen dengan Tepat: Kita bisa menempatkan elemen di dalam grid menggunakan properti seperti grid-column dan grid-row.

5.
Pertama kita akan membuat fungsi untuk menghapus dan mengedit produk. Kedua fugsi ini akan mengambil object produk yang sudah jadi berdasarkan id yang ada pada request nanti fungsi edit akan membuat form produk baru dan form tersebut akan menggantikan produknya sementara fungsi delete akan menghapusproduk tersebut.

Selanjutnya kita akan mempercantik tampilan website menggunakan Tailwind CSS. Pertama tambahkan <script src="https://cdn.tailwindcss.com">. kita akan mendekorasi html menggunakan metode external style sheet berikutnya kita konfigurasi static file pada settigs.py lalu kita akan membuat global.css yang akan diletakan pada direktori static/css. global.css berfungsi sebagai template Utama css. kita akan mendekorasi register page dan login page. Aksen website ini didominasi oleh warna oranye. kita akan membuat field dimana user bisa memasukan username dan password menggunakan input serta kita akan membuat tombol untuk register dan login menggunakan button yang diwarnai oranye dan akan berubah warna saat di hover. pada halaman register dan login kita juga akan menambahkan judul menggunakan h1 yang diberi warna ungu.

Setelah itu kita akan membuat navigation bar yang akan menyesuaikan dengan ukuran layar. 
kita akan membuat 2 versi navigation bar untuk desktop dan mobile. Warna dari navigation bar ini adalah oranye dengan fitur button logout berwarna merah kode dari button tersebt untuk menghubungkannya dengan fungsi logout adalah :

```bash 
<a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
             Logout
            </a>. 
```

Navigation bar juga menampilkan teks nama dari website ini dan navigation bar ini juga menampilkan nama user yang sudah login menggunakan {{ user.username }}. untuk navigation bar pada mobile, kita akan menambahkan hamburger untuk membuat design lebih minimalis menggunakan queryselector button yang diikuti dengan event listener. Setelah itu kita akan membuat template card yang akan berguna sebagai template dari masing-masing produk yang ditambahkan. Card ini berwarna putih dan berisi atribut-atribut yang dimiliki produk yaitu nama, deskripsi dan Harga. Kita juga akan menambahkan tombol edit produk dan delete yang akan menuju ke tampilan fungsinya masing-masing dengan kode sebagai berikut :

```bash 
<a href="{% url 'main:edit_product' product_entry.pk %}">
            <button class="bg-yellow-500 text-white py-1 px-3 rounded  hover:bg-yellow-600">Edit</button>
        </a>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button class="bg-red-500 text-white py-1 px-3 rounded hover:bg-red-600">Delete</button>
        </a>
```

Card ini juga memiliki shadow yang diberi warna kuning sebagai efek glow.

Berikutnya kita akan mempercantik halaman main view. pada bagian teratas halaman main kita akan menulis judul dengan h1 ukuran besar berupa "Welcome to WeMart by Muhammad Fadhlan Arradhi - 2306240061!" dengan tulisan berwarna ungu. Dibawahnya akan tersedia informasi mengenai nama dari akun yang sedang terlogin. kita akan membuat container dengan tag container sebagai pembatas yang akan menampung produk Utama yang terdapat pada context di show_main pada views.py. container ini mengandung section berwarna putih yang diisi dengan atribut-atribut pada context yang diisi dengan tag h5 dan p. pada container ini juga terdapat informasi session cookie terakhir yang ditampilkan melalui tag h5. section pada container ini juga diberi efek shadow berwarna kuning tua. berikutnya kita akan menampilkan produk-produk yang ada menggunakan loop yang akan menampilkan semua produk berdasarkan template card yang sudah dibuat. Jika belum ada produk yang ditambahkan maka conditional akan mengarahkan program menuju kode handle yang akan memberi tulisan "Belum ada produk ditambahkan" yang disertai gambar. gambar ini disimpan pada folder static/image dengan kode :

```bash <p class="text-red-600 text-3xl text-center font-bold mt-4">Belum Ada Produk Baru Ditambahkan</p>, <img src="{% static 'image/umaru.gif' %}" alt="Sad face" class="shadow-md shadow-amber-300">. jika sudah ada produk yang ditambahkan maka loop produk akan dilakukan dengan kode : 
{% for product_entry in product_entries %}
      {% include 'card_product.html' with product_entry=product_entry %}
{% endfor %}
```

lalu terdapat tombol untuk menambahkan produk serta logout yang terletak di bagian paling Bawah main

Selanjutnya kita akan mempercantik tampilan dari tambahkan produk dan edit produk. pada kedua halaman ini, kita akan membuat section berwarna putih yang diberi efek shadow berwarna kuning. section ini akan menampung form yang nantinya akan berisikan field-field pada models. kita tidak perlu membuat input secara eksplisit karena django telah menghandle input untuk masing-masing jenis field tersebut. kita cukup mendesign button untuk menambahkan produk yang berwarna hijau. kita juga membuat tombol untuk kembali ke halaman utama bagi user yang tidak jadi menambahkan atau mengedit produk. tombol tersebut diberi link dengan kode :

```bash
<a href="{% url 'main:show_main' %}" class="font-medium text-orange-400 hover:text-orange-500">
        <button type="submit" class="bg-orange-400 text-white font-semibold px-6 py-3 rounded-lg hover:bg-orange-500 transition duration-300 ease-in-out w-full">
          Kembali
        </button>
      </a>
```
tombol-tombol ini juga kakan berubah warna ketika di hover.

========================================================================

Tugas 6 PBP

1.
manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web antara lain:

- JavaScript memungkinkan pengembang untuk menangani event pada halaman web, seperti klik, scroll, dan input pengguna, yang memperkaya pengalaman pengguna.

- Dengan JavaScript, pengembang dapat membuat permintaan HTTP asinkron tanpa perlu memuat ulang halaman menggunakan AJAX dan Fetch API. Hal ini meningkatkan performa aplikasi dan memberikan pengalaman yang lebih halus.

- JavaScript didukung di hampir semua browser modern, membuatnya menjadi pilihan yang sangat fleksibel dan serbaguna dalam pengembangan web.


2. 
await berungsi untuk menunggu respon hasil dari fungsi async. Jika kita tidak menggunakan fungsi await, maka kode JavaScript akan terus berjalan tanpa menunggu respons server, sehingga kita tidak dapat langsung menggunakan data yang diterima dari server.

3.
Decorator csrf_exempt digunakan pada view Django yang menerima request POST dari AJAX untuk menonaktifkan pemeriksaan CSRF (Cross-Site Request Forgery) pada request tersebut. Secara default, Django menerapkan perlindungan CSRF untuk mencegah serangan CSRF, di mana form POST memerlukan token CSRF yang valid.
Namun, dalam konteks AJAX request, sering kali token CSRF tidak disertakan, sehingga request akan ditolak. Dengan menambahkan decorator csrf_exempt, kita memberi pengecualian pada view tersebut agar dapat menerima request POST tanpa token CSRF

4.
Pembersihan data input pengguna dilakukan di backend untuk memastikan keamanan dan integritas aplikasi. Meskipun sanitasi di frontend dapat membantu mencegah beberapa jenis serangan seperti XSS (Cross-Site Scripting) atau input tidak valid, hal tersebut tidak cukup karena:

- Pengguna yang jahat bisa mem-bypass validasi frontend dengan menggunakan alat seperti cURL atau Postman untuk mengirim request langsung ke server.

- Validasi dan pembersihan di backend memastikan bahwa input yang diterima oleh server adalah aman dan sesuai dengan aturan yang diharapkan, terlepas dari bagaimana data tersebut dikirim.

- Backend memiliki kontrol penuh terhadap bagaimana data diproses dan disimpan, sehingga meminimalkan risiko kebocoran data atau eksploitasi.
Karena itu, validasi dan pembersihan input dilakukan di backend sebagai lapisan keamanan tambahan, meskipun validasi di frontend tetap penting untuk pengalaman pengguna yang baik.

5.
pertama kita akan membuat fungsi untuk menambahkan produk menggunakan AJAX. fungsi  ini dimulai dengan decorator @csrf_exempt yang menonaktifkan pengecekan CSRF pada request tersebut, memastikan bahwa AJAX POST dapat dikirim tanpa memerlukan token CSRF. Selain itu, @require_POST digunakan untuk membatasi bahwa hanya request POST yang diizinkan.
Ketika request diterima, data produk seperti nama, deskripsi, dan harga diambil dari request POST, dan pengguna yang sedang login (dari request.user) juga dicatat sebagai pemilik produk tersebut. Data ini kemudian digunakan untuk membuat objek Products, yang selanjutnya disimpan ke database menggunakan metode save(). Jika produk berhasil disimpan, view merespons dengan status 201 Created, yang menunjukkan bahwa entri produk baru berhasil dibuat.

Selanjutnya kita menggunakan AJAX GET untuk mengambil data produk. Kode ini terdapat pada fungsi getProductEntries() yang mengirimkan request ke server untuk mengambil data produk dalam format JSON, dan refreshProductEntries() yang memperbarui daftar produk pada halaman dengan data yang diterima. fungsi dibawah ini bertugas untuk mengambil data produk yang hanya milik pengguna yang sedang login. Kita akan memfilter data produk berdasarkan request.user.

```bash
async function getProductEntries(){
    return fetch("{% url 'main:show_json' %}").then((res) => res.json())
}
```

Sementara fungsi refreshProductEntries() dibawah ini berfungsi untuk untuk mengupdate serta memberi tampilan data produk di halaman secara dinamis menggunakan hasil dari AJAX GET. Dengan ini, pengguna tidak perlu mereload halaman untuk melihat daftar produk yang mereka miliki. Jika file JSON tidak tersedia, maka fungsi ini akan memberikan tampilan dimana produk baru belum ditambahkan. Jika sudah fungsi ini akan menampilkan produk menggunakan kode card yang sudah kita definisikan sebelumnya. Akan tetapi, terdapat perubahaan pada cardnya dimana object yang ada pada model diubah menjadi item.fields. Selain itu kita juga melakukan DOMPurify untuk pembersihan data. 

```bash
async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const ProductEntries = await getProductEntries();
    let htmlString = "";
    let classNameString = "";

    if (ProductEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/umaru.gif' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada product ditambahkan.</p>
            </div>
        `;
    }
    else {
        classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6"
        ProductEntries.forEach((item) => {
          const name = DOMPurify.sanitize(item.fields.name);
          const description = DOMPurify.sanitize(item.fields.description);
          const price = DOMPurify.sanitize(item.fields.price);
            htmlString += `
            <div class="bg-white-500 shadow-md shadow-amber-300 rounded-lg p-6">
                <img src="${item.fields.image_url}" alt="Gambar Produk" class="w-full h-48 object-contain rounded-lg mb-4 center">
                <h2 class="text-xl font-semibold">${name}</h2>
                <p class="text-gray-600 mt-2">${description}</p>
                <p class="text-indigo-600 font-bold mt-2">Rp. ${price}</p>
    
                <div class="mt-4 flex">
                    <a href="/edit-product/${item.pk}">
                        <button class="bg-yellow-500 text-white py-1 px-3 rounded  hover:bg-yellow-600">Edit</button>
                    </a>
                    <a href="/delete-product/${item.pk}">
                        <button class="bg-red-500 text-white py-1 px-3 rounded hover:bg-red-600">Delete</button>
                    </a>
                </div>
            </div>
            `;
        });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}

```

Selanjutnya kita akan




