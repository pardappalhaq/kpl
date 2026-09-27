def enkripsi_caesar(teks_asli, geser):
    """Menggeser huruf plaintext sesuai nilai kunci."""
    
    hasil = ""

    for char in teks_asli:

        # Jika huruf kapital
        if char.isupper():
            hasil += chr((ord(char) + geser - 65) % 26 + 65)

        # Jika huruf kecil
        elif char.islower():
            hasil += chr((ord(char) + geser - 97) % 26 + 97)

        # Jika angka, spasi, atau simbol, biarkan tetap
        else:
            hasil += char

    return hasil


def dekripsi_caesar(teks_sandi, geser):
    """Mengembalikan ciphertext menjadi plaintext."""
    
    return enkripsi_caesar(teks_sandi, -geser)


def brute_force_caesar(teks_sandi):
    """Mencoba seluruh kemungkinan kunci dari 1 sampai 25."""

    print("\n=== MEMULAI SERANGAN BRUTE FORCE ===")

    for kunci_coba in range(1, 26):
        hasil_coba = dekripsi_caesar(teks_sandi, kunci_coba)

        print(
            f"Kunci {kunci_coba:02d} -> "
            f"Hasil Dekripsi: {hasil_coba}"
        )

if __name__ == "__main__":

    # Pesan asli dan kunci rahasia
    pesan_asli = "Praktikum TRPL IPB University"
    kunci_rahasia = 5

    # 1. Enkripsi plaintext menjadi ciphertext
    teks_terkunci = enkripsi_caesar(
        pesan_asli,
        kunci_rahasia
    )

    print(f"Pesan Asli  : {pesan_asli}")
    print(f"Kunci Geser : {kunci_rahasia}")
    print(f"Hasil Sandi : {teks_terkunci}")

    # 2. Dekripsi ciphertext menjadi plaintext
    teks_terbuka = dekripsi_caesar(
        teks_terkunci,
        kunci_rahasia
    )

    print(f"Dekripsi    : {teks_terbuka}")

    # 3. Simulasi serangan brute force
    brute_force_caesar(teks_terkunci)