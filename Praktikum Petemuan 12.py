class Mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    def __str__(self):
        return (f"NIM         : {self.nim}\n"
                f"Nama        : {self.nama}\n"
                f"Tugas       : {self.tugas}\n"
                f"UTS         : {self.uts}\n"
                f"UAS         : {self.uas}\n"
                f"Nilai Akhir : {self.nilai_akhir:.1f}")


class DataMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah_data(self):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        self.data_mahasiswa[nim] = Mahasiswa(nim, nama, tugas, uts, uas)
        print("Data Mahasiswa berhasil ditambahkan!")

    def lihat_data(self):
        print("\nDaftar Nilai Mahasiswa:")
        print("===============================================================================================")
        print("|   NO   |    NIM    |       NAMA      |    TUGAS    |     UTS     |     UAS     |    AKHIR   |")
        print("===============================================================================================")
        if not self.data_mahasiswa:
            print("|                                  TIDAK ADA DATA MAHASISWA                                   |")
        else:
            no = 1
            for nim, mhs in self.data_mahasiswa.items():
                print(f"| {no:^6} | {nim:^8} | {mhs.nama:<15} | {mhs.tugas:^11.1f} | {mhs.uts:^11.1f} | {mhs.uas:^11.1f} | {mhs.nilai_akhir:^10.1f} |")
                no += 1
        print("===============================================================================================")

    def ubah_data(self):
        nim = input("Masukkan NIM Mahasiswa yang akan diubah: ")
        if nim in self.data_mahasiswa:
            print("Data ditemukan. Silakan masukkan data baru.")
            nama = input("Masukkan Nama: ")
            tugas = float(input("Masukkan Nilai Tugas: "))
            uts = float(input("Masukkan Nilai UTS: "))
            uas = float(input("Masukkan Nilai UAS: "))
            self.data_mahasiswa[nim] = Mahasiswa(nim, nama, tugas, uts, uas)
            print("Data Mahasiswa berhasil diubah!")
        else:
            print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

    def hapus_data(self):
        nim = input("Masukkan NIM yang akan dihapus: ")
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

    def cari_data(self):
        nim = input("Masukkan NIM yang dicari: ")
        if nim in self.data_mahasiswa:
            print("\nData Mahasiswa:")
            print(self.data_mahasiswa[nim])
        else:
            print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

    def main(self):
        print("PROGRAM INPUT NILAI MAHASISWA")
        while True:
            opsi = input("\nSilahkan pilih opsi [L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar = ").lower()

            if opsi == 'k':
                print("Terima kasih telah menggunakan program ini.")
                break
            elif opsi == 't':
                self.tambah_data()
            elif opsi == 'l':
                self.lihat_data()
            elif opsi == 'u':
                self.ubah_data()
            elif opsi == 'h':
                self.hapus_data()
            elif opsi == 'c':
                self.cari_data()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


# Jalankan program
if __name__ == "__main__":
    app = DataMahasiswa()
    app.main()
