def min_coins(amount, coins, memo=None):
    if memo is None:
        memo = {}

    # Jika jumlah uang yang ingin dicapai adalah 0, tidak perlu koin
    if amount == 0:
        return 0
    
    # Jika jumlah uang negatif, tidak mungkin mencapainya
    if amount < 0:
        return float('inf')
    
    # Cek apakah hasil sudah ada di memo
    if amount in memo:
        return memo[amount]

    # Inisialisasi jumlah koin minimum
    min_coins_needed = float('inf')

    # Coba setiap koin dan hitung jumlah koin yang diperlukan
    for coin in coins:
        result = min_coins(amount - coin, coins, memo)
        min_coins_needed = min(min_coins_needed, result + 1)

    # Simpan hasil di memo
    memo[amount] = min_coins_needed
    return min_coins_needed

# Fungsi utama untuk mendapatkan input dari pengguna
def main():
    amount = int(input("Masukkan jumlah uang yang ingin dicapai: "))
    coins = list(map(int, input("Masukkan daftar nilai koin (pisahkan dengan spasi): ").split()))

    result = min_coins(amount, coins)

    if result == float('inf'):
        print("Tidak mungkin mencapai jumlah tersebut dengan koin yang diberikan.")
    else:
        print(f"Jumlah minimum koin yang diperlukan: {result}")

# Jalankan program
if __name__ == "__main__":
    main()
