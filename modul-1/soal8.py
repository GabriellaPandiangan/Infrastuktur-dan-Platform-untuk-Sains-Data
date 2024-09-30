def reverse_words(input_string):
    # Memecah string menjadi daftar kata-kata
    words = input_string.split()
    
    # Membalik setiap kata dan menyimpannya dalam daftar baru
    reversed_words = [word[::-1] for word in words]
    
    return reversed_words

# Fungsi utama untuk mendapatkan input dari pengguna
def main():
    input_string = input("Masukkan string: ")
    result = reverse_words(input_string)
    print(result)

# Jalankan program
if __name__ == "__main__":
    main()
