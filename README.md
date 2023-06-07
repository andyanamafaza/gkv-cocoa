# Gkv-Cocoa

Proyek mata kuliah Grafika Komputer dan Visualisasi.
Dibuat dengan menggunakan bahasa pemrograman Python dan library Plotly Express untuk membuat visualisasi data area lahan kakao di Indonesia berdasarkan provinsi dari tahun 2014 hingga 2021.

## Deskripsi Proyek

Gkv-Cocoa adalah proyek yang bertujuan untuk membantu visualisasi data mengenai luas areal kakao di setiap provinsi di Indonesia selama rentang waktu 2014 hingga 2021. Program ini menggunakan peta choropleth dan grafik time series untuk memberikan pemahaman yang lebih baik tentang perubahan luas area tanam kakao di seluruh provinsi. Data yang digunakan berasal dari sumber yang terpercaya, yaitu [Satu Data Pertanian](https://satudata.pertanian.go.id/assets/docs/metadata/Areal-Kakao.xls).

## Fitur

Program ini memiliki beberapa fitur yang dapat memperkaya pengalaman pengguna:

1. **Peta Choropleth**:\
   Program menampilkan peta choropleth yang interaktif untuk memvisualisasikan luas areal kakao di setiap provinsi di Indonesia. Setiap provinsi diwarnai berdasarkan luas area tanam kakao yang dimiliki. Warna yang digunakan untuk menggambarkan jumlah luas area kakao ditentukan berdasarkan skala warna yang telah ditentukan sebelumnya. Pengguna dapat melihat luas area kakao untuk setiap provinsi dengan mengarahkan kursor ke provinsi tersebut. Selain itu, pengguna juga dapat memilih tahun tertentu menggunakan animasi yang tersedia.

2. **Grafik Time Series**:\
   Program menyajikan grafik time series yang menampilkan perubahan luas areal kakao dari tahun ke tahun untuk provinsi-provinsi yang dipilih. Pengguna dapat memilih provinsi-provinsi yang ingin ditampilkan pada grafik tersebut menggunakan dropdown. Grafik ini memungkinkan pengguna untuk melihat tren perubahan luas areal kakao seiring berjalannya waktu.

3. **Informasi Provinsi**:\
   Program ini juga menyediakan informasi tambahan mengenai setiap provinsi. Ketika pengguna mengarahkan kursor ke provinsi tertentu pada peta choropleth, informasi provinsi seperti nama provinsi, luas area tanam kakao, dan tahun terkait akan ditampilkan.

4. **Navigasi yang Mudah**:\
   Program ini dilengkapi dengan antarmuka yang intuitif dan navigasi yang mudah digunakan. Pengguna dapat dengan mudah beralih antara peta choropleth dan grafik time series. Selain itu, tombol zoom dan pan tersedia di peta choropleth untuk memudahkan pengguna dalam memeriksa detail provinsi secara lebih mendalam.

## Cara Menjalankan

Berikut adalah langkah-langkah untuk menjalankan Program ini di lingkungan lokal Anda:

1. Pastikan Anda memiliki Python versi 3.x terinstal di sistem Anda.

2. Clone repositori Gkv-Cocoa ke direktori lokal Anda:

   ```bash
   git clone https://github.com/andyanamafaza4/gkv-cocoa
   ```

3. Masuk ke direktori proyek:

   ```bash
   cd gkv-cocoa
   ```

4. Instal semua library yang dibutuhkan dengan menjalankan perintah berikut di terminal:

   ```bash
   pip install -r requirements.txt
   ```

5. Jalankan Program dengan perintah berikut:

   ```bash
   python main.py
   ```
## Anggota Kelompok
|Nama|NIM|
|--|--|
|[Andyana Lilmuttaqina Mafaza](https://github.com/andyanamafaza4)|G6401211002|
|[Muhamad Surya Fauzan](https://github.com/Sxugi)|G6401211011|
|[Muhammad Giyas Wisnu Rizqi ](https://github.com/madgiyas)|G6401211091|
|[Zhafran Nazhifa Defa](https://github.com/zhafrannazhifa)|G6401211097|
|[Malikus Syafaadi Nurfaza](https://github.com/Malikusfz)|G6401211121|

## Referensi
- [Plotly Choropleth Maps in Python](https://plotly.com/python/choropleth-maps/)
- [Plotly Time-Series in Python](https://plotly.com/python/time-series/)
- [Dash User Guide](https://dash.plotly.com/)
- [Indonesia GeoJSON](https://github.com/superpikar/indonesia-geojson)
- [Luas Areal Kakao Menurut Provinsi di Indonesia, 2014-2021](https://satudata.pertanian.go.id/assets/docs/metadata/Areal-Kakao.xls)
