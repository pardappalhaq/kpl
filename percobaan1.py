def enkripsi_caesar(teks_asli, geser):
    """Menggeser huruf plaintext sesuai nilai kunci."""

    hasil = ""

    for i in range(len(teks_asli)):
        char = teks_asli[i]

        # Enkripsi huruf kapital
        if char.isupper():
            hasil += chr((ord(char) + geser - 65) % 26 + 65)

        # Enkripsi huruf kecil
        elif char.islower():
            hasil += chr((ord(char) + geser - 97) % 26 + 97)

        # Jika karakter berupa angka, spasi, atau simbol, biarkan utuh
        else:
            hasil += char

    return hasil


def dekripsi_caesar(teks_sandi, geser):
    """Mendekripsi kembali dengan geseran berlawanan arah."""

    return enkripsi_caesar(teks_sandi, -geser)


def brute_force_caesar(teks_sandi):
    """Mencoba menebak seluruh kemungkinan kunci (1 s.d. 25)."""

    print("\n=== MEMULAI SERANGAN BRUTE FORCE ===")

    for kunci_coba in range(1, 26):
        hasil_coba = dekripsi_caesar(teks_sandi, kunci_coba)

        print(
            f"Dicoba Kunci {kunci_coba:02d} -> "
            f"Hasil Dekripsi: {hasil_coba}"
        )


# --- SKENARIO UJI COBA JALANNYA PROGRAM ---
if __name__ == "__main__":

    pesan_asli = "Praktikum TRPL IPB University"
    kunci_rahasia = 5

    # 1. Proses mengubah plaintext menjadi ciphertext
    teks_terkunci = enkripsi_caesar(
        pesan_asli,
        kunci_rahasia
    )

    print(f"Pesan Asli  : {pesan_asli}")
    print(f"Kunci Geser : {kunci_rahasia}")
    print(f"Hasil Sandi : {teks_terkunci}")

    # 2. Proses mengembalikan ciphertext ke plaintext
    teks_terbuka = dekripsi_caesar(
        teks_terkunci,
        kunci_rahasia
    )

    print(f"Dekripsi    : {teks_terbuka}")

    # 3. Simulasi serangan tebak kunci oleh hacker
    brute_force_caesar(teks_terkunci)