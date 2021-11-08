# Contribution Page
Semua orang bisa memberikan kontribusi dalam bentuk apapun, baik kode, dokumentasi, atau penjelasan. Ada beberapa hal yang perlu diketahui atau dipelajari khususnya terkait struktur repository.

## Penamaan
- Untuk penamaan folder, gunakan format kapital di setiap kata, misalnya `Artifical Neural Network`
- Untuk penamaan file penjelasan, gunakan nama `README.MD` sehingga bisa langsung terindeks ketika folder dibuka.
- Tambahkan nama kalian sebagai kontributor di file `CONTRIBUTOR.MD`. Tambahkan jika belum ada.
- Untuk file kodingan, masukan di dalam folder `core`.

Sehingga dalam satu folder, kurang lebih strukturnya seperti ini (Misal dengan nama Artificial Neural Network)

```
├─Artificial Neural Network
  ├─ core
  │  ├─ ArtificialNeuralNetwork.py
  │  ├─ test.py
  ├─ README,.MD
  ├─ CONTRIBUTOR.MD
  ├─ requirements.txt

```

## Kode
- Jika ingin berkontribusi melalui kode program, silakan buat dalam bahasa Python.
- Pastikan nama class dan file kode program sama dengan nama folder namun tanpa spasi.
- Penulisan kode mengikuti standar penulisan bahasa Python.
- Penulisan variabel, fungsi, dan method harus menggunakan bahasa yang mudah dipahami dan berbahasa Inggris.
- Untuk keperluan testing, silakan buat file `test.py`.
- Jika ingin membuat algoritma versi sendiri, silakan buat class dengan format `NamaAlgoritmaNamaKamu.py`
- Untuk keperluan testingnya, silakan buat file dengan format `testNamaAlgoritmaNamaKamu.py`
- Jika ada library tambahan, jangan lupa masukan di file requirements.txt

## Penjelasan
- Penjelasan harus mudah dipahami.
- Gunakan analogi yang mudah dipahami.
- Bebas memasukan gambar selagi saling berkaitan dengan materi.
- Walaupun bebas, harus merujuk pada beberapa sumber terpercaya seperti jurnal, penelitian ilmiah, dan lain sebagainya.
- Selalu tambahkan rujukan di sesi paling bawah penjelasan.
- Isi penjelasan tidak boleh jauh dari algoritmanya.

## Proses kontribusi
- Clone repository ini atau fork jika mau.
- Selalu buat branch baru ketika ingin mengubah atau melakukan kontribusi sekecil apapun.
- Penamaan branch bebas asal mudah dipahami dan tidak bertele-tele.
- Selalu masukan pesan komit dengan jelas.
- Selalu isi judul dan perubahan di saat akan merge request.
- Branch yang sudah dimerge akan dihapus dari origin.

## Terima kasih
Bagi yang ingin mengembangkan saya ucapkan terima kasih banyak. Mari bangun repositori ini dengan lebih baik supaya memberikan manfaat bagi banyak orang.