# Dataset perpustakaan 
data_perpustakaan = {
    "2023001": {
        "judul": "Pemrograman Python untuk Pemula",
        "pengarang": "Andi Susanto",
        "tahun_terbit": 2021,
        "status": "tersedia",
        "halaman": 210
    },
    "2023002": {
        "judul": "Data Science dengan Python",
        "pengarang": "Darrell Lokadeva Lim",
        "tahun_terbit": 2020,
        "status": "dipinjam",
        "halaman": 350
    },
    "2023003": {
        "judul": "Algoritma dan Struktur Data",
        "pengarang": "Fiona",
        "tahun_terbit": 2019,
        "status": "tersedia",
        "halaman": 400
    },
    "2023004": {
        "judul": "Pengantar Machine Learning",
        "pengarang": "Miranda",
        "tahun_terbit": 2022,
        "status": "tersedia",
        "halaman": 280
    },
    "2023005": {
        "judul": "Basis Data untuk Pemula",
        "pengarang": "Noor Ichsan Maulana",
        "tahun_terbit": 2018,
        "status": "dipinjam",
        "halaman": 320
    },
    "2023006": {
        "judul": "Jaringan Komputer Dasar",
        "pengarang": "Agus Pratama",
        "tahun_terbit": 2021,
        "status": "tersedia",
        "halaman": 154
    }
}

# Tambah fungsi tabulate untuk menampilkan data dalam bentuk tabel
from tabulate import tabulate
headers = ["ID Buku", "Judul", "Pengarang", "Tahun Terbit", "Status", "Halaman"]

# Fungsi untuk menampilkan menu utama
def menu():
    print("=== Menu Perpustakaan ===")
    print("1. Tampilkan buku")
    print("2. Tambahkan buku baru")
    print("3. Ganti informasi buku")
    print("4. Hapus data buku")
    print("5. Keluar")

def tampilkan_semua_buku(): # Option 1.1, menampilkan semua buku
    print("\n=== Daftar Semua Buku di Perpustakaan ===")

    # Menampilkan semua data buku yang ada.
    table_data = []
    for id_buku, info_buku in data_perpustakaan.items():
        table_data.append([ # pakai .get() untuk menghindari error jika value tidak ada
            id_buku,
            info_buku.get("judul", "-"),
            info_buku.get("pengarang", "-"),
            info_buku.get("tahun_terbit", "-"),
            info_buku.get("status", "-"),
            info_buku.get("halaman", "-")
        ]) 
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def tampilkan_buku_berdasarkan_id(): # Option 1.2, menampilkan buku berdasarkan ID
    id_buku_input = input("Masukkan ID Buku:")
    table_data = []
    found = False

    # Mencari buku berdasarkan ID yang dimasukkan
    for id_buku, info_buku in data_perpustakaan.items():
        if id_buku_input == id_buku:
            found = True
            table_data.append([
                id_buku,
                info_buku.get("judul", "-"),
                info_buku.get("pengarang", "-"),
                info_buku.get("tahun_terbit", "-"),
                info_buku.get("status", "-"),
                info_buku.get("halaman", "-")
            ])
            break
    
    # Menampilkan hasil pencarian
    if found == True:
        print(f"\nDetail Buku dengan ID {id_buku_input}:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("ID Buku tidak ditemukan.")
        return


def tambahkan_buku_baru(): # Option 2, menambahkan buku baru
    id_buku_baru = input("Masukkan ID Buku Baru: ")
    if id_buku_baru in data_perpustakaan:
        print("ID Buku sudah ada. Silahkan gunakan ID lain.")
        return
    # Input data buku baru
    judul_baru = input("Masukkan Judul Buku: ")
    pengarang_baru = input("Masukkan Pengarang Buku: ")
    tahun_terbit_baru = int(input("Masukkan Tahun Terbit Buku: "))
    status_baru = input("Masukkan Status Buku (tersedia/dipinjam): ")
    if status_baru not in ["tersedia", "dipinjam"]: # Validasi status buku
        print("Status tidak valid. Gunakan kata 'tersedia' atau 'dipinjam'.")
        return
    halaman_baru = int(input("Masukkan Jumlah Halaman Buku: "))
    
    # Opsi untuk menyimpan data buku baru
    print("Apakah anda ingin menyimpan data buku baru?")
    print("1. Ya \n2. Tidak")
    save_option = input("Pilih opsi: ")

    # Simpdan data
    if save_option == "1":
        data_perpustakaan[id_buku_baru] = {
            "judul": judul_baru,
            "pengarang": pengarang_baru,
            "tahun_terbit": tahun_terbit_baru,
            "status": status_baru,
            "halaman": halaman_baru
        }
        print("Data buku baru berhasil disimpan.")
        return
    
    # Batal simpan
    elif save_option == "2":
        print("Data buku baru tidak disimpan.")
        return
    
    # Pilihan tidak valid
    else:
        print("Pilihan tidak valid. Data buku baru tidak disimpan.")
        return

def ganti_informasi_buku(): # Option 3, mengganti informasi buku
    id_buku_ganti = input("Masukkan ID buku yang ingin diganti infromasinya: ")
    
    if id_buku_ganti in data_perpustakaan: # Cek apakah ID buku ada
        print(f"Detail Buku dengan ID {id_buku_ganti}:")
        table_data = [[
            id_buku_ganti,
            data_perpustakaan[id_buku_ganti].get("judul", "-"),
            data_perpustakaan[id_buku_ganti].get("pengarang", "-"),
            data_perpustakaan[id_buku_ganti].get("tahun_terbit", "-"),
            data_perpustakaan[id_buku_ganti].get("status", "-"),
            data_perpustakaan[id_buku_ganti].get("halaman", "-")
        ]] 

        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        # Opsi untuk melanjutkan update
        print("\nApakah anda ingin melanjutkan update informasi buku ini?")
        print("1. Ya \n2. Tidak")
        lanjutkan = input("Pilih opsi: ")
        
        # Lanjut update
        if lanjutkan == "1":
            print("Masukkan kolom yang ingin diganti:")
            print("1. Judul \n2. Pengarang \n3. Tahun Terbit \n4. Status \n5. Halaman")
            kolom_ganti = input("Pilih kolom (1-5): ")

            kolom_map = {
                '1': 'judul',
                '2': 'pengarang',
                '3': 'tahun_terbit',
                '4': 'status',
                '5': 'halaman'
            }

            # Bagian mengganti kolom
            if kolom_ganti in kolom_map:
                while True:
                    nama_kolom = kolom_map[kolom_ganti]
                    if kolom_ganti in ['1', '2']:
                        info_baru = input(f"Masukkan informasi baru untuk {nama_kolom}: ")
                        break
                    elif kolom_ganti in ['3', '5']:
                        try:
                            info_baru = int(input(f"Masukkan informasi baru untuk {nama_kolom} (berupa angka): "))
                            break
                        except ValueError:
                            print("Input tidak valid. Harus berupa angka.")
                    elif kolom_ganti == '4':
                        info_baru = input(f"Masukkan informasi baru untuk {nama_kolom} (tersedia/dipinjam): ")
                        if info_baru not in ["tersedia", "dipinjam"]:
                            print("Status tidak valid. Gunakan kata 'tersedia' atau 'dipinjam'.")
                        else:
                            break

                print("Apakah anda yakin ingin mengganti informasi ini? \n1. Ya \n2. Tidak")
                konfirmasi_ganti = input("Pilih opsi: ")

                # Ganti data
                if konfirmasi_ganti == "1":
                    data_perpustakaan[id_buku_ganti][nama_kolom] = info_baru
                    print("Informasi buku berhasil diganti.")
                    return
                
                # Batal ganti
                elif konfirmasi_ganti == "2":
                    print("Penggantian informasi dibatalkan.")
                    return
            else:
                print("Kolom tidak valid.")
                return
        
        # Batal update      
        elif lanjutkan == "2":
            print("Update dibatalkan.")
            return
    else: 
        print("ID buku tidak ditemukan.")
        return
    
def hapus_data_buku(): # Option 4.1, menghapus data buku
    id_buku_hapus = input("Masukkan ID buku yang ingin dihapus: ")
    if id_buku_hapus in data_perpustakaan: # Cek apakah ID buku ada
        print(f"Detail Buku dengan ID {id_buku_hapus}:")
        table_data = [[
            id_buku_hapus,
            data_perpustakaan[id_buku_hapus].get("judul", "-"),
            data_perpustakaan[id_buku_hapus].get("pengarang", "-"),
            data_perpustakaan[id_buku_hapus].get("tahun_terbit", "-"),
            data_perpustakaan[id_buku_hapus].get("status", "-"),
            data_perpustakaan[id_buku_hapus].get("halaman", "-")
        ]]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        # Memberi konfirmasi sebelum menghapus
        print("Apakah anda yakin ingin menghapus data buku ini?")
        print("1. Ya \n2. Tidak")
        konfirmasi = input("Pilih opsi: ")

        # Hapus data
        if konfirmasi == "1":
            del data_perpustakaan[id_buku_hapus]
            print("Data buku berhasil dihapus.")
            return
        
        # Batal hapus       
        elif konfirmasi == "2":
            print("Penghapusan data buku dibatalkan.")
            return
    else:
        print("ID buku tidak ditemukan.")
        return

def hapus_data_tertentu_dari_buku(): # Option 4.2, menghapus data tertentu dari buku
    id_buku_hapus = input("Masukkan ID buku yang ingin dihapus: ")  
    if id_buku_hapus in data_perpustakaan: # Cek apakah ID buku ada
        print(f"Detail Buku dengan ID {id_buku_hapus}:")
        table_data = [[
            id_buku_hapus,
            data_perpustakaan[id_buku_hapus].get("judul", "-"),
            data_perpustakaan[id_buku_hapus].get("pengarang", "-"),
            data_perpustakaan[id_buku_hapus].get("tahun_terbit", "-"),
            data_perpustakaan[id_buku_hapus].get("status", "-"),
            data_perpustakaan[id_buku_hapus].get("halaman", "-")
        ]]
    else: 
        print("ID buku tidak ditemukan.")
        return
    
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    # Konfirmasi sebelum menghapus data yang diinginkan
    print("\nApakah anda yakin ingin menghapus data tertentu dari buku ini?")
    print("1. Ya \n2. Tidak")
    konfirmasi = input("Pilih opsi: ") 
    
    # Hapus kolom
    if konfirmasi == "1":
        print("Masukkan data kolom yang ingin dihapus:")
        print("1. Judul \n2. Pengarang \n3. Tahun Terbit \n4. Status \n5. Halaman")
        kolom_hapus = input("Pilih kolom (1-5): ")

        kolom_map = {
            '1': 'judul',
            '2': 'pengarang',
            '3': 'tahun_terbit',
            '4': 'status',
            '5': 'halaman'
        }

        # Bagian menghapus kolom
        if kolom_hapus in kolom_map:
            nama_kolom = kolom_map[kolom_hapus]
            print(f"Apakah anda yakin ingin menghapus informasi di kolom {nama_kolom}? \n1. Ya \n2. Tidak")
            konfirmasi_hapus = input("Pilih opsi: ")

            # Hapus data kolom
            if konfirmasi_hapus == "1":
                del data_perpustakaan[id_buku_hapus][nama_kolom]
                print("Informasi buku berhasil dihapus.")
                return
            
            # Batal hapus kolom
            elif konfirmasi_hapus == "2":
                print("Penghapusan informasi dibatalkan.")
                return
        else:
            print("Kolom tidak valid.")
            return

    # Batal hapus
    elif konfirmasi == "2":
        print("Penghapusan data dibatalkan.")
        return
    else:
        print("Pilihan tidak valid.")
        return

    
# Fungsi utama untuk menjalankan program
def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        # Opsi menampilkan buku (Read)
        if pilihan == '1':
            while True:
                print("\n=== Menu Tampilkan Buku ===")
                print("1. Tampilkan semua buku \n2. Tampilkan buku berdasarkan ID\n3. Keluar ke menu utama")
                sub_pilihan = input("Pilihlah sub-menu (1-3): ")

                # Tampilkan semua buku
                if sub_pilihan == '1':
                    if len(data_perpustakaan) == 0:
                        print("Data perpustakaan kosong.")
                    else:
                        tampilkan_semua_buku()
                        
                # Tampilkan buku berdasarkan ID
                elif sub_pilihan == '2':
                    if len(data_perpustakaan) == 0:
                        print("Data perpustakaan kosong.")
                    else:
                        print("Daftar ID Buku yang tersedia:")
                        for index in data_perpustakaan:
                            print(f"- {index}")
                        tampilkan_buku_berdasarkan_id()
                
                # Keluar ke menu utama
                elif sub_pilihan == '3':
                    break
                else: 
                    print("Pilihan tidak valid. Pilihlah menu yang tersedia.")

        # Opsi tambahkan buku baru (Create)
        elif pilihan == '2':
            while True:
                print("\n=== Menu Tambahkan Buku Baru ===")
                print("1. Tambahkan buku baru \n2. Keluar ke menu utama")
                sub_pilihan = input("Pilihlah sub-menu (1-2): ")

                # Tambah buku baru
                if sub_pilihan == '1':
                    tambahkan_buku_baru()
                
                # Keluar ke menu utama
                elif sub_pilihan == '2':
                    break
                else: 
                    print("Pilihan tidak valid. Pilihlah menu yang tersedia.")

        # Opsi ganti informasi buku (Update)
        elif pilihan == '3':
            while True:
                print("\n=== Menu Ganti Informasi Buku ===")
                print("1. Ganti informasi buku \n2. Keluar ke menu utama")
                sub_pilihan = input("Pilihlah sub-menu (1-2): ")

                # Ganti informasi buku
                if sub_pilihan == '1':
                    print("Daftar ID Buku yang tersedia:")
                    for id_buku in data_perpustakaan:
                        print(f"- {id_buku}")
                    ganti_informasi_buku()

                # Keluar ke menu utama
                elif sub_pilihan == '2':
                    break
                else:
                    print("Pilihan tidak valid. Pilihlah menu yang tersedia.")
            
        # Opsi hapus data buku (Delete)
        elif pilihan == '4':
            while True:
                print("\n=== Menu Hapus Data Buku ===")
                print("1. Hapus buku dari dataset \n2. Hapus data tertentu dari buku \n3. Keluar ke menu utama")
                sub_pilihan = input("Pilihlah sub-menu (1-3): ")
                
                # Hapus buku dari dataset
                if sub_pilihan == '1':
                    for id_buku in data_perpustakaan:
                        print(f"- {id_buku}")
                    hapus_data_buku()

                # Hapus data tertentu dari buku
                elif sub_pilihan == '2':
                    for id_buku in data_perpustakaan:
                        print(f"- {id_buku}")
                    hapus_data_tertentu_dari_buku()
                
                # Keluar ke menu utama
                elif sub_pilihan == '3':
                    break
                else:
                    print("Pilihan tidak valid. Pilihlah menu yang tersedia.")

        # Opsi keluar
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program perpustakaan! Sampai jumpa!")
            break
        # Opsi tidak valid
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang tersedia.")

# Menjalankan "main" saat file dieksekusi langsung
if __name__ == "__main__":
    main()

    
