def isfloat(variable):
    '''
    fungsi untuk melakukan validasi apakah sebuah tipe data dapat diubah menjadi tipe float
    contoh:
    isfloat('7.5') bernilai True
    isfloat(7.5) bernilai True
    isfloat('aku') bernilai False
    isfloat(7) bernilai True
    
    parameter:
    variable : suatu data yang ingin diuji
    '''
    try:
        float(variable)
    except ValueError:
        return False
    else:
        return True

#Inisiasi nilai keluar = False agar bisa masuk ke APLIKASI UTAMA
keluar = False
val = False

#APLIKASI UTAMA
while keluar == False:

    # Validasi variabel input pilihan_user agar user hanya dapat memilih 1/2/3 saja
    while val == False:
        pilihan_user = input('1. Belanja 2. Belajar 3.Exit ')
        if pilihan_user.isdigit():
            pilihan_user = int(pilihan_user)
            if 1 <= pilihan_user <= 3:
                break
            else:
                print('Pilihan Hanya 1-3 Saja!')
        else:
            print('Pilihan Menu Utama Tidak Boleh Mengandung Huruf!')
    
    # Proses dari pilihan_user apabila nilai yang diinput = 1 (Belanja)
    if pilihan_user == 1:
        print('Pilihan Menu: ')
        print('1. Daging Ayam Rp 40.000/kg ')
        print('2. Daging Sapi Rp 80.000/kg ')
        print('3. Daging Salmon Rp 100.000/kg ')
        
        # Validasi variabel input input_makanan agar user hanya dapat memilih 1/2/3 saja
        while val == False:
            input_makanan = input('Pilih nomor menu (1/2/3) : ')
            if input_makanan.isdigit():
                input_makanan = int(input_makanan)
                if 1 <= input_makanan <= 3:
                    break
                else:
                    print('Pilihan Hanya 1-3 Saja!')
            else:
                print('Input Menu Makanan Tidak Boleh Mengandung Huruf!')

        # Proses hasil input_makanan tervalidasi
        if input_makanan == 1:
            menu = 'Daging Ayam'
            harga = 40000
        elif input_makanan == 2:
            menu = 'Daging Sapi'
            harga = 80000
        else:
            menu = 'Daging Salmon'
            harga = 100000
        
        # Validasi variabel input qty agar user hanya dapat memasukan bilangan bulat
        while val == False:
            qty = input(f'Masukan Quantity {menu} (kg) = ')
            if qty.isdigit():
                qty = int(qty)
                break
            else:
                print('Quantity tidak boleh mengandung huruf atau bilangan tidak bulat')

        #Print output dari pilihan_user = 1 (Belanja)
        print(f'Anda membeli {menu} sebanyak {qty} kg seharga Rp {qty*harga},- ')


    # Proses dari pilihan_user apabila nilai yang diinput = 2 (Belajar)
    elif pilihan_user == 2:
        print('Pilihan Belajar: ')
        print('1. Hitung Luas Segitiga ')
        print('2. Hitung Luas Trapesium ')
        
        # Validasi variabel input input_materi agar user hanya dapat memilih 1/2 saja
        while val == False:
            input_materi = input('Materi yang hendak Anda pilih (1/2) :')
            if input_materi.isdigit():
                input_materi = int(input_materi)
                if 1 <= input_materi <= 2:
                    break
                else:
                    print('Pilihan hanya 1 atau 2 saja')
            else:
                print('Pilihan tidak boleh mengandung huruf')

        # Proses hasil input_materi = 1 (Hitung Luas Segitiga)
        if input_materi == 1:
            bangunan = 'segitiga'

            # Validasi variabel input alas_segitiga agar dapat berupa bilangan float tetapi tidak dapat huruf atau karakter
            while val == False:
                alas_segitiga = input('Masukan alas dari segitiga : ')
                if isfloat(alas_segitiga):
                    alas_segitiga = float(alas_segitiga)
                    break
                else:
                    print('Tidak boleh memasukkan selain angka')

            # Validasi variabel input tinggi_segitiga agar dapat berupa bilangan float tetapi tidak dapat huruf atau karakter
            while val == False:
                tinggi_segitiga = input('Masukan tinggi dari segitiga : ')
                if isfloat(tinggi_segitiga):
                    tinggi_segitiga = float(tinggi_segitiga)
                    break
                else:
                    print('Tidak boleh memasukkan selain angka')
            
            #Penghitungan Luas Segitiga
            luas = (alas_segitiga * tinggi_segitiga) /2

        # Proses hasil input_materi = 2 (Hitung Luas Trapesium)
        elif input_materi == 2:
            bangunan = 'trapesium'

             # Validasi variabel input sisi_atas agar dapat berupa bilangan float tetapi tidak dapat huruf atau karakter
            while val == False:
                sisi_atas = input('Masukan sisi atas trapesium : ')
                if isfloat(sisi_atas):
                    sisi_atas = float(sisi_atas)
                    break
                else:
                    print('Tidak boleh memasukkan selain angka')

             # Validasi variabel input sisi_bawah agar dapat berupa bilangan float tetapi tidak dapat huruf atau karakter
            while val == False:
                sisi_bawah = input('Masukan sisi bawah trapesium : ')
                if isfloat(sisi_bawah):
                    sisi_bawah = float(sisi_bawah)
                    break
                else:
                    print('Tidak boleh memasukkan selain angka')

             # Validasi variabel input tinggi_trap agar dapat berupa bilangan float tetapi tidak dapat huruf atau karakter
            while val == False:
                tinggi_trap = input('Masukan tinggi trapesium : ')
                if isfloat(tinggi_trap):
                    tinggi_trap = float(tinggi_trap)
                    break
                else:
                    print('Tidak boleh memasukkan selain angka')

            # Penghitungan luas trapesium
            luas = (sisi_atas + sisi_bawah) * tinggi_trap/2

        # Print output pilihan_user = 2 (Belajar)
        print(f'luas {bangunan} adalah {round(luas, 2)} satuan luas')

    # Proses dari pilihan_user apabila nilai yang diinput = 3 (Exit)
    else:
        # keluar dari APLIKASI UTAMA
        keluar = True
        break

    # Validasi variabel input input_exit agar user hanya dapat memilih y/n saja
    while val == False:
        input_exit = input('Anda mau keluar dari aplikasi (y/n) : ')
        if input_exit == 'y' or input_exit == 'n':
            break
        else:
            print('Pilihan hanya (y) atau (n) saja')
    
    # Proses apabila user menginput input_exit = y 
    if input_exit == 'y':
        # pengubahan nilai variable keluar menjadi True agar keluar dari APLIKASI UTAMA
        keluar = True 


# BAGIAN LUAR DARI APLIKASI UTAMA
print('Terimakasih Sudah Menggunakan Aplikasi Kami!')