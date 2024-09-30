
import pandas as pd
import csv


# Fungsi untuk membaca file CSV dan menyimpan datanya ke dalam dictionary
def baca_csv_ke_dictionary(nama_file):
    data_mahasiswa = {}
    try:
        with open(nama_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            header = csv_reader.fieldnames
            print(f"Header yang ditemukan: {header}")  # Menampilkan header untuk pengecekan
            
            for row in csv_reader:
                if 'Nama' in row:  # Cek apakah kolom 'Nama' ada
                    nama = row['Nama']
                    try:
                        nilai = list(map(int, row['Nilai'].split(',')))  # Mengubah nilai menjadi list angka
                        data_mahasiswa[nama] = nilai
                    except ValueError:
                        print(f"Error: Nilai tidak valid untuk mahasiswa {nama}.")
                else:
                    print("Error: Kolom 'Nama' tidak ditemukan.")
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
    return data_mahasiswa
