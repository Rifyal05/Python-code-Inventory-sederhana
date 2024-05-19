# Import exer_modul sebagai modul 'exorcist'
import exer_modul as exorcist

# Looping atau perulangan untuk menjalankan pogram berulang kali
while True:
        # Daftar pilihan yang dapat di jalankan oleh program ini
        print()
        print('Menu Manajemen Stok Barang:')
        print('1. Tambah Barang')
        print('2. Hapus Barang')
        print('3. Tampilkan Data')
        print('4. Hitung Jumlah Data')
        print('5. Pencarian Data')
        print('6. Edit Data')
        print('7. Test')
        print('8. Keluar')
        print()
        # Input pengguna yang berisi pilihan dari daftar pilihan menu
        pilihan = int(input('Masukan pilihan anda: '))
        # Percabangan (digunakan untuk mengeksekusi input jika memenuhi syarat pilihan)
        if pilihan == 1:
            exorcist.tambah_barang()
        elif pilihan == 2:
            exorcist.hapus_barang()
        elif pilihan == 3:
            exorcist.tampil_barang()
        elif pilihan == 4:
            exorcist.hitung_jumlah_data()
        elif pilihan == 5:
            exorcist.cari_data()
        elif pilihan == 6:
            exorcist.edit_data()
        elif pilihan == 7: # Digunakan untuk mengakhiri program
            exorcist.test() 
        elif pilihan == 8:
            print('==================================================================')
            print('Program telah berhasil di berhentikan, Terimakasih.... ')
            print('==================================================================')
            break #menghentikan perulangan
        else:
            # Pesan yang ditampilkan jika input dari pengguna tidak memenuhi syarat atau tidak ada dalam daftar pilihan
            print('==================================================================')
            print('Input yang anda masukan tidak valid, harap masukan input yang valid [1/2/3/4/5/6/7/8]!!')
            print('Ulangi proses')
            print('==================================================================')
            print()