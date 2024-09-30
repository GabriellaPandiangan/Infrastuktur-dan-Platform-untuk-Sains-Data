class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    def hitung_usia(self):
        from datetime import datetime
        current_year = datetime.now().year
        usia = current_year - self.tahun_terbit
        return usia

# Membuat 3 objek dari class Buku dengan judul yang jarang
buku1 = Buku("Lautan Tanpa Ujung", "Ayu Lestari", 2015)
buku2 = Buku("Puncak Kesunyian", "Rizky Dharma", 2018)
buku3 = Buku("Jejak di Atas Awan", "Mira Sari", 2020)

# Menampilkan informasi dan usia masing-masing buku
for buku in (buku1, buku2, buku3):
    buku.tampilkan_info()
    print(f"Usia Buku: {buku.hitung_usia()} tahun\n")


