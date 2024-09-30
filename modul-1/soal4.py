import pandas as pd
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# membaca file dan menyimpan data dalam dict
def bacacsv(filename):
    data = {}
    with open(filename, mode='r') as file:
        baca_csv = csv.reader(file)
        next(baca_csv)  
        for row in baca_csv:
            nama= row[0]
            nilai = list(map(float, row[1:]))  # jadikan float
            data[nama] = nilai  
    return data

# menghitung rata2
def hitungrata(data):
    rata2 = {}
    for nama, nilai in data.items():
        if nilai: 
            rata2[nama] = sum(nilai) / len(nilai)
    return rata2

# menemukan nilai tertinggi dan terendah
def caritertinggi_terendah(rata2):
    tertinggi = max(rata2, key=rata2.get)
    terendah = min(rata2, key=rata2.get)
    return tertinggi, terendah

# main program
def main():
    filename = 'D:/KULIAH/SEM 3/Prak Infranstruktur/Tugas-1/modul-1/nilai.csv'
    data = bacacsv(filename)

    # menghitung rata2 tiap mhs
    rata2 = hitungrata(data)

    print("Rata-rata nilai tiap mahasiswa:")
    for name, avg in rata2.items():
        print(f"{name}: {avg:.2f}")

    # menemukan nilai tertinggi dan terendah
    tertinggi, terendah = caritertinggi_terendah(rata2)

    print(f"\nMahasiswa dengan nilai rata-rata tertinggi: {tertinggi} ({rata2[tertinggi]:.2f})")
    print(f"Mahasiswa dengan nilai rata-rata terendah: {terendah} ({rata2[terendah]:.2f})")

if __name__ == "__main__":
    main()