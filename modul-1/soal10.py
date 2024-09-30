def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Mengembalikan indeks jika ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Mengembalikan -1 jika tidak ditemukan

def main():
    # Daftar hanya berisi angka genap
    even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    # Minta input dari pengguna
    target = int(input("Masukkan angka yang ingin dicari: "))

    # Cek apakah nilai yang dicari adalah angka genap
    if target % 2 != 0:
        print("Nilai yang dicari adalah angka ganjil. Tidak dapat ditemukan di dalam daftar.")
    else:
        # Lakukan pencarian biner
        result = binary_search(even_numbers, target)

        if result != -1:
            print(f"Angka {target} ditemukan di indeks {result}.")
        else:
            print(f"Angka {target} tidak ditemukan di dalam daftar.")

# Jalankan program
if __name__ == "__main__":
    main()
