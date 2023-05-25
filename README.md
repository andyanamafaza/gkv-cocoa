# Gkv-Coffee
Proyek mata kuliah Grafika Komputer dan Visualisasi.
Dibuat dengan menggunakan bahasa pemrograman Python dan library Plotly Express untuk membuat visualisasi data produktivitas kopi di Indonesia berdasarkan provinsi dari tahun 2014 hingga 2021.
## Fitur

Aplikasi ini memiliki dua fitur utama:

1. Peta Choropleth:
   Aplikasi menampilkan peta choropleth yang menunjukkan data produktivitas kopi di setiap provinsi di Indonesia. Setiap provinsi diwarnai berdasarkan luas areal kopi yang dimiliki. Warna yang digunakan untuk mewakili jumlah luas areal kopi ditentukan oleh skala warna yang ditentukan. Pengguna dapat memilih tahun tertentu menggunakan animasi dan melihat luas areal kopi untuk setiap provinsi dengan mengarahkan kursor ke provinsi tersebut.

2. Grafik Time Series:
   Aplikasi juga menyajikan grafik time series yang menampilkan perubahan luas areal kopi dari tahun ke tahun untuk provinsi-provinsi yang dipilih. Pengguna dapat memilih provinsi-provinsi yang ingin ditampilkan pada grafik tersebut menggunakan dropdown. Grafik akan menampilkan tren perubahan luas areal kopi seiring waktu untuk provinsi-provinsi yang dipilih.


## How to Run
1. Install library yang dibutuhkan dengan menjalankan perintah berikut di terminal:
``` bash
python -m pip install -r requirements.txt
```
2. Jalankan program dengan menjalankan perintah berikut di terminal:
``` bash
python main.py
```
3. Peta akan ditampilkan di browser.

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
- [Luas Areal Kopi Menurut Provinsi di Indonesia, 2014-2021](https://satudata.pertanian.go.id/assets/docs/metadata/Areal-Kopi.xls)
