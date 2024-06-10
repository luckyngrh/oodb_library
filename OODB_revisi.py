import sqlite3
from prettytable import PrettyTable

#Home Page
print("SELAMAT DATANG DI DATABASE PERPUSTAKAAN MINI")
print("Kegiatan yang dapat dilakukan : \n 1.Tambah buku \n 2.Tampilkan daftar Buku \n 3.Hapus Buku \n 4.Cari Buku \n")
pilihan =input("Masukkan pilihan : ")

# Definisikan kelas Buku
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
    
# Definisikan kelas DatabaseBuku
class DatabaseBuku:
    def __init__(self, nama_database):
        self.nama_database = nama_database
        self.conn = sqlite3.connect(nama_database)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS buku (judul TEXT, penulis TEXT, tahun_terbit INTEGER)")

    def tambah_buku(self, buku):
        self.cursor.execute("INSERT INTO buku VALUES (?, ?, ?)", (buku.judul, buku.penulis, buku.tahun_terbit))
        self.conn.commit()
        print("Buku berhasil ditambahkan ke database.")

    def hapus_buku(self, judul):
        self.cursor.execute("DELETE FROM buku WHERE judul = ?", (judul,))
        self.conn.commit()
        print("Buku berhasil dihapus dari database.")

    def cari_buku(self, judul):
        self.cursor.execute("SELECT * FROM buku WHERE judul = ?", (judul,))
        result = self.cursor.fetchall()
        if result:
            print("Buku ditemukan dalam database.")
            table = PrettyTable(["Judul","Penulis","Tahun Terbit"])
            table.align = 'l'  # Mengatur penataan teks menjadi rata kiri
            # Menambahkan baris data ke tabel
            for row in result:
                table.add_row(row)
            # Menampilkan tabel 
            print(table)
        else:
            print("Buku tidak ditemukan dalam database.")

    def tampilkan_semua_buku(self):
        self.cursor.execute("SELECT * FROM buku ORDER BY judul asc")
        results = self.cursor.fetchall()
        if results:
            print("Daftar Buku:")
            table = PrettyTable(["Judul","Penulis","Tahun Terbit"])
            #Untuk mengambil table tanpa perubahan field gunakan : description[0] for description in self.cursor.description
            table.align = 'l'  # Mengatur penataan teks menjadi rata kiri
            # Menambahkan baris data ke tabel
            for row in results:
                table.add_row(row)
            # Menampilkan tabel 
            print(table)
        else:
            print("Database kosong.")

    def __del__(self):
        self.cursor.close()
        self.conn.close()

#Pilihan Kegiatan
if int(pilihan) == 1 :
    jd_bk = input("Masukkan Judul Buku : ")
    png_bk = input("Masukkan Nama Pengarang : ")
    th_bk = input("Masukkan Tahun Terbit : ")
    db_buku = DatabaseBuku("perpustakaan.db")
    buku1 = Buku(jd_bk,png_bk, th_bk)
    db_buku.tambah_buku(buku1)
elif int(pilihan) == 2 :
    db_buku = DatabaseBuku("perpustakaan.db")
    db_buku.tampilkan_semua_buku()
elif int(pilihan) == 3 :
    jd_bk = input("Masukkan Judul Buku yang ingin dihapus : ")
    db_buku = DatabaseBuku("perpustakaan.db")
    db_buku.hapus_buku(jd_bk)
elif int(pilihan) == 4 :
    jd_bk = input("Masukkan Judul Buku yang ingin dicari : ")
    db_buku = DatabaseBuku("perpustakaan.db")
    db_buku.cari_buku(jd_bk)
else :
    print("Pilihan Anda Salah")