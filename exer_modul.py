# Data list kosong
data_barang = []


# Fungsi untuk tambah barang
def tambah_barang():
    nama_barang   = str(input('Masukan nama barang: ')) # Input Nama Barang
    nama_barang   = nama_barang.upper() # Mengkonversikan input kedalam bentuk UPPERCASE
    jumlah_barang = int(input('Masukkan jumlah barang: ')) # Input Jumlah barang
    data_baru = {'nama barang': nama_barang, 'jumlah barang': jumlah_barang} # Sebuah dictionary key yang berisi input dari pengguna dengan format 'nama barang : value dan jumlah barang : value
    data_barang.append(data_baru) # Memasukkan dictionary key kedalam (list 'data_barang')
    return()

# Fungsi untuk menghapus barang
def hapus_barang():
    input_pilihan  = str(input('Silahkan pilih berdasarkan apa data di hapus? (Nama/Index) :' )) # Input pengguna untuk memasukkan pilihannya
    input_pilihan  = input_pilihan.capitalize() # Mengonversi Input kedalam Kapitalisasi
    while True:
        if input_pilihan == 'Index':  # Mengecek apakah input memenuhi syarat untuk menjalankan kode local selanjutnya atau lompat cek poin berikutnya
            index_barang = int(input('Masukan index barang : ')) # Pengguna akan disuruh menginput dalam bentuk integer
            data_barang.pop(index_barang) # Menghapus data barang berdasarkan index
            print()
            print(f"barang dengan index {index_barang} telah berhasil dihapus") # Menampilkan pesan jika data barang telah berhasil di hapus
        elif input_pilihan == 'Nama': # Cek poin ke 2 untuk mengecek apakah input memenuhi syarat untuk menjalankan kode atau tidak. Jika tidak, eksekusi kode akan lompat ke cek point selanjutnya
            print('Jika anda memilih untuk menghapus dengan nama, anda harus memasukkan nama lengkap barang yang telah anda input.') # Menginformasikan bahwa anda harus menginput nama lengkap barang yang telah anda input jika anda memilih untuk menghapus berdasarkan nama
            nama_barang = str(input('Masukan nama barang: ')).upper() # Mengkonversikan input kedalam bentuk UPPERCASE
            for barang in data_barang: # Digunakan untuk mengiterasi setiap data barang kedalam list (data_barang)
                if barang['nama barang'] == nama_barang: # Cek poin untuk mengecek apakah iterasi dalam data 'barang[yang berformat = nama barang : value]' sama dengan input yang dimasukkan pengguna ('nama_barang') atau tidak.
                    data_barang.remove(barang) # Fungsi remove akan dijalankan jika cek poin terpenuhi, dengan menghapus barang berdasarkan iterasi yang berasal dari input pengguna
                    print(f"Barang dengan nama '{nama_barang}' telah berhasil dihapus") # Kode yang di jalankan jika fungsi remove dijalankan
                    break # menghentikan perulangan
            else:
                # Kode yang akan dijalankan jika cek poin sebelumnya tidak terpenuhi
                print(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")
        else:
             # Kode yang akan dijalankan jika cek poin sebelumnya tidak terpenuhi
             print('Input yang anda masukan tidak valid, harap masukan input yang valid [Nama/Index]')
             print('Ulangi proses')
             print()
        break # Menghentikan perulangan
    return()

# Fungsi untuk Menampilkan barang
def tampil_barang():
    print()
    if not data_barang: # Cek poin yang berisi fungsi yang akan dijalankan jika data_barang[list] tidak berisi apapun alias kosong
        print("Data Barang Kosong")
    else: # Cek poin yang akan dijalankan jika cek poin sebelumnya tidak terpenuhi syaratnya  
        print('Berikut daftar barang yang telah anda input:')
        # Digunakan untuk menampilkan data barang dengan index barang tersebut.
        for nomor, barang in enumerate(data_barang):  
            print(f"{nomor}. {barang['nama barang']} dengan jumlah barang =  {barang['jumlah barang']}") 
    return()
#  Fungsi untuk menghitung jumlah data yang telah di input
def hitung_jumlah_data():
    print()
    print(f"Jumlah data barang yang tersimpan berjumlah: {len(data_barang)} data barang") # Menampilkan jumlah data yang telah diinput

# Fungsi untuk mencari data di dalam program
def cari_data():
    keyword = str(input('Masukan keyword untuk mencari data: ')).upper() # Menginput keyword kemudia mengubahnya kedalam format UPPERCASE
    found = False # Pernyataan bahwa barang belum di temukan
    print(f'Berikut barang yang di temukan berdasarkan kata kunci {keyword}:') 
    i = 1 # Iterasi untuk penomoran daftar barang yang di tampilkan
    for barang in data_barang:
        if keyword in barang['nama barang']: # cek point untuk mengecek apakah input pengguna ada dalam data_barang atau tidak
            print(f"{i}. {barang['nama barang']} dengan jumlah barang = {barang['jumlah barang']}") # menampilkan hasil yang ditemukan ditambah dengan penomoran
            found = True # Pernyataan bahwa data barang telah di temukan
            i+=1 # Iterasi yang digunakan untuk penomoran dengan format +1 untuk setiap data barang
    if not found: # Cek point yang akan di eksekusi jika input yang dimasukkan pengguna tidak di temukan
        print()
        print(f"Uhhh maaf tapi barang yang anda cari menggunakan kata kunci '{keyword}' tidak ditemukan.") # Pesan yang akan muncul setelah kode di eksekusi
        return(cari_data())

# Fungsi untuk mengedit data
def edit_data():
    print()
    index_barang = int(input('Masukan index barang : ')) # Pengguna diminta memasukkan input dalam bentuk integer
    nama_barang = str(input('Masukan nama barang: ')).upper() # pengguna diminta memasukan input nama dengan string
    jumlah_barang = int(input('Masukkan jumlah barang: ')) # Pengguna diminta memasukkan input jumlah barang dalam bentuk integer
    data_barang[index_barang] = {'nama barang': nama_barang, 'jumlah barang': jumlah_barang} # hasil yang di input yang berbntuk dictionary tersebut akan dimemasukkan kedalam data list[data_barang] dan mengubahnya
    print(f"Data barang dengan index {index_barang} telah diubah.") # Informasi mengenai barang dalam index tertentu telah di ganti
    return()