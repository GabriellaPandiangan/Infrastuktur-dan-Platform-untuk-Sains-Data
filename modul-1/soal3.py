#include <iostream>
using namespace std;

int main() {
    const int PIN_CORRECT = 123456;  // PIN yang benar, sekarang 6 digit
    const int MAX_ATTEMPTS = 3;      // Batas percobaan
    double saldo = 5000.0;           // Saldo awal
    int inputPIN;
    int attempts = 0;
    bool authenticated = false;
    
    // Meminta pengguna memasukkan PIN dengan batas 3 kali percobaan
    while (attempts < MAX_ATTEMPTS) {
        cout << "Masukkan PIN 6 digit Anda: ";
        cin >> inputPIN;
        
        if (inputPIN == PIN_CORRECT) {
            authenticated = true;
            break;
        } else {
            attempts++;
            cout << "PIN salah. Anda memiliki " << (MAX_ATTEMPTS - attempts) 
                 << " percobaan tersisa." << endl;
        }
    }
    
    // Jika pengguna berhasil memasukkan PIN yang benar
    if (authenticated) {
        double jumlahPenarikan;
        cout << "PIN benar.\n";
        cout << "Saldo Anda: Rp" << saldo << endl;
        
        // Meminta jumlah penarikan
        cout << "Masukkan jumlah yang ingin ditarik: Rp";
        cin >> jumlahPenarikan;
        
        // Cek apakah saldo cukup
        if (jumlahPenarikan > saldo) {
            cout << "Kesalahan: Saldo tidak mencukupi untuk penarikan sebesar Rp" 
                 << jumlahPenarikan << endl;
        } else {
            // Penarikan berhasil, kurangi saldo
            saldo -= jumlahPenarikan;
            cout << "Penarikan berhasil sebesar Rp" << jumlahPenarikan << endl;
            cout << "Saldo akhir Anda: Rp" << saldo << endl;
        }
    } else {
        // Jika PIN salah 3 kali
        cout << "Anda telah memasukkan PIN salah 3 kali. Akses diblokir." << endl;
    }

    return 0;
}
