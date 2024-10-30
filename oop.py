class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
    try:
        # Meminta input panjang dan lebar dari pengguna
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))

        # Membuat objek persegi panjang terlebih dahulu
        persegi_panjang = PersegiPanjang(panjang, lebar)

        # Validasi input apakah panjang dan lebar lebih besar dari nol
        if persegi_panjang.panjang <= 0 or persegi_panjang.lebar <= 0:
            print("Panjang dan lebar harus lebih besar dari nol.")
            return

        # Menampilkan informasi objek
        print(persegi_panjang)

        # Menampilkan keliling
        print("Keliling:", persegi_panjang.keliling(), "cm")

        # Menampilkan luas
        print("Luas:", persegi_panjang.luas(), "cm^2")

    except ValueError:
        print("Input harus berupa angka. Silakan masukkan nilai numerik untuk panjang dan lebar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Memanggil fungsi main jika script dijalankan secara langsung
if __name__ == "__main__":
    main()
