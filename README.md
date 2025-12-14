# Sistem Manajemen Perpustakaan (Capstone Project Modul 1)
Repositori ini berisi program berbasis Python untuk mengelola data buku perpustakaan. Program ini dibuat sebagai **Capstone Project Modul 1** dengan menerapkan konsep dasar pemrograman Python, struktur data (Dictionary), dan logika alur program (Control Flow) yang ketat.

## 📋 Deskripsi Proyek
Program ini adalah aplikasi *Command Line Interface* (CLI) yang berfungsi sebagai sistem manajemen basis data sederhana untuk perpustakaan. Program memungkinkan pengguna untuk melakukan operasi **CRUD** (Create, Read, Update, Delete) pada koleksi buku.

Alur program ini dirancang mengikuti **Flowchart Logika Program** secara presisi, memastikan setiap input pengguna divalidasi dan setiap proses memiliki konfirmasi keamanan sebelum data diubah atau dihapus.

## ✨ Fitur Utama
Program ini mencakup fitur-fitur berikut berdasarkan kode sumber:
* **Menampilkan Data (Read):**
  * Menampilkan seluruh daftar buku dalam format tabel yang rapi.
  * Mencari dan menampilkan detail buku spesifik berdasarkan **ID Buku (Primary Key)**.

* **Menambahkan Data (Create):**
  * Input data buku baru (ID, Judul, Pengarang, Tahun, Status, Halaman).
  * **Validasi Duplikasi:** Mencegah input ID yang sudah ada di database.
  * Konfirmasi penyimpanan sebelum data dimasukkan ke sistem.

* **Memperbarui Data (Update):**
  * Mengedit informasi buku yang sudah ada berdasarkan ID.
  * Fleksibilitas untuk memilih kolom spesifik yang ingin diubah (Judul, Pengarang, dll).

* **Menghapus Data (Delete):**
  * **Hapus Buku:** Menghapus seluruh entri buku berdasarkan ID.
  * * **Hapus Data Tertentu:** Fitur tambahan untuk menghapus nilai kolom tertentu tanpa menghapus seluruh buku (Fitur Ekstra).
  * **Validasi Input:** Menangani input menu yang tidak valid dengan notifikasi error agar program tidak *crash*.

##🛠️ Prasyarat & Instalasi
Program ini membutuhkan **Python 3.x** dan *library* eksternal untuk format tabel.

1. **Clone repositori ini:**
```bash
git clone https://github.com/username/library-management-system.git

```
2. **Install Library Tabulate:**
Program ini menggunakan `tabulate` untuk mempercantik tampilan output.
```bash
pip install tabulate

```
3. **Jalankan Program:**
```bash
python Darrell_Capstone1.py

```

## 📂 Struktur Data
Data disimpan menggunakan **Nested Dictionary** di mana `ID Buku` bertindak sebagai *Primary Key*, memungkinkan pencarian data yang cepat dan efisien.

```python
data_perpustakaan = {
    "2023001": {
        "judul": "Pemrograman Python untuk Pemula",
        "pengarang": "Andi Susanto",
        # ... atribut lainnya
    }
}

```

## 🔄 Alur Program (Flowchart Alignment)
Program ini telah lulus uji kesesuaian dengan diagram alur (Flowchart) yang ditentukan:
1. **Menu Utama:** Loop utama yang menangani navigasi ke sub-menu.
2. **Sub-Menu Logic:** Setiap menu (Read, Create, Update, Delete) memiliki sub-menu sendiri sesuai desain.
3. **Error Handling:** Notifikasi otomatis jika ID tidak ditemukan atau data duplikat.

## 👤 Pembuat 
**Darrell Lokadeva Lim** *Capstone Project Data Science / Python Programming*
