import random

def word_guessing_game():
    # Daftar kata yang akan ditebak
    words = ["python", "programming", "developer", "computer", "science", "game"]
    secret_word = random.choice(words)  # Memilih kata secara acak
    attempts = 6  # Jumlah percobaan
    guessed_letters = set()  # Menyimpan huruf yang sudah ditebak

    print("Selamat datang di permainan tebak kata!")
    print("Saya telah memilih sebuah kata. Cobalah tebak kata tersebut.")
    
    while attempts > 0:
        # Menampilkan status kata dengan huruf yang sudah ditebak
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print(f"\nKata: {display_word}")
        print(f"Kesempatan tersisa: {attempts}")
        
        guess = input("Tebakan Anda (masukkan satu huruf): ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Tolong masukkan hanya satu huruf.")
            continue
        
        if guess in guessed_letters:
            print("Anda sudah menebak huruf ini sebelumnya.")
            continue
        
        guessed_letters.add(guess)  # Menyimpan huruf yang sudah ditebak
        
        if guess in secret_word:
            print(f"Bagus! Huruf '{guess}' ada dalam kata.")
        else:
            print(f"Maaf, huruf '{guess}' tidak ada dalam kata.")
            attempts -= 1  # Mengurangi kesempatan jika tebakan salah
        
        # Memeriksa apakah pengguna sudah menebak semua huruf
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Selamat! Anda berhasil menebak kata '{secret_word}'!")
            break
    else:
        print(f"Maaf, Anda telah kehabisan kesempatan. Kata yang benar adalah '{secret_word}'.")

# Menjalankan permainan
word_guessing_game()
