def menu():
    print("MENU ABSENSI SEKOLAH")
    print("1. Tampilkan address array")
    print("2. Tampilkan address dari semua index array")
    print("3. Masukkan data absensi siswa")
    print("4. Tampilkan daftar absensi")
    print("5. Keluar")

def main():
    jumlah = int(input("Masukkan jumlah siswa: "))
    absen = [""] * jumlah
    running = True

    while running:
        menu()

        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print(f"\nAddress array absensi: {id(absen)}")

        elif choice == 2:
            print("\nAddress dari setiap index array:")
            for i in range(jumlah):
                print(f"Address absen[{i}] = {id(absen[i])}")

        elif choice == 3:
            print(f"\nMasukkan {jumlah} nama siswa yang hadir:")
            for i in range(jumlah):
                while True:
                    nama = input(f"Nama siswa ke-{i+1}: ")

                    if nama.strip() == "":
                        print("Nama tidak boleh kosong!")
                    else:
                        absen[i] = nama
                        break

            print("\nData absensi berhasil disimpan!")

        elif choice == 4:
            print("\nDAFTAR ABSENSI SISWA")
            for i in range(jumlah):
                if absen[i] == "":
                    print(f"Absen {i+1}: Belum diisi")
                else:
                    print(f"Absen {i+1}: {absen[i]}")

        elif choice == 5:
            running = False
            print("\nProgram selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()