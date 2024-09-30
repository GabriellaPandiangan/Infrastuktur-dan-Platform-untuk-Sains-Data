# Fungsi untuk memeriksa apakah suatu angka adalah bilangan prima
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fungsi untuk menghasilkan bilangan prima hingga jumlah yang dibutuhkan
def generate_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Fungsi untuk mencetak pola berdasarkan bilangan prima
def print_prime_pattern(rows):
    total_primes_needed = sum(range(1, rows + 1))  # Hitung total bilangan prima yang dibutuhkan
    primes = generate_primes(total_primes_needed)  # Hasilkan bilangan prima sebanyak yang dibutuhkan

    index = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(primes[index], end=" ")
            index += 1
        print()

# Jumlah baris pola yang ingin dicetak
rows = 4
print_prime_pattern(rows)
