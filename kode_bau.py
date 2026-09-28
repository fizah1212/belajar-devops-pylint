"""Modul demonstrasi fungsi kalkulasi matematika sederhana."""


def hitung_penjumlahan(angka_pertama, angka_kedua):
    """Menjumlahkan dua buah angka integer.

    Args:
        angka_pertama (int): Nilai bilangan pertama.
        angka_kedua (int): Nilai bilangan kedua.

    Returns:
        int: Hasil penjumlahan kedua bilangan.
    """
    return angka_pertama + angka_kedua


def main():
    """Fungsi utama program."""
    hasil = hitung_penjumlahan(10, 20)
    print(f"Hasil penjumlahan: {hasil}")


if __name__ == "__main__":
    main()