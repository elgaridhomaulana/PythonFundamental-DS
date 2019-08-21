val = True
keluar = False

while keluar == False:
    out = ''
    print('\nMENU UTAMA')

    while val == True:
        pil_menu= input('Apa yang Mau Anda Gambar? \n (1) Segitiga Siku-Siku \n (2) Segitiga Sama Kaki \n (3) Persegi \n (4) Exit \nPilihan = ')
        if pil_menu.isdigit():
            if 1 <= int(pil_menu) <= 4:
                break
            else:
                print('Pilihan 1-4 Saja!')
        else:
            print('Masukan Bilangan Bulat 1-4!')

    if pil_menu == '1':

        while val == True:
            pil_sss = input('Bentuk dari Segitiga Siku-Siku: \n (1) Siku Atas \n (2) Siku Bawah \nPilihan Bentuk = ')
            if pil_sss.isdigit():
                if 1 <= int(pil_sss) <= 2:
                    break
                else:
                    print('Pilihan 1-2 Saja!')
            else:
                print('Masukan Bilangan Bulat 1-2!')
        
        while val == True:
            tinggi = input('Berapa Tinggi dari Segitiga? (Maksimal 30) ? ')
            if tinggi.isdigit():
                tinggi = int(tinggi)
                if 1 <= tinggi <= 30:
                    break
                elif tinggi <= 0:
                    print('Tidak boleh 0 atau negatif!')
                else:
                    print('Tidak boleh lebih dari 30!')
            else:
                print('Tidak boleh float atau huruf!')

        print('')

        if pil_sss == '1':
            bentuk = 'Segita Siku-Siku - Siku Atas'
            # i = 0
            # while i < tinggi:
            #     j = 0
            #     while j < tinggi-i:
            #         out += '*' 
            #         j += 1
            #     out += '\n'
            #     i += 1
            for i in range(tinggi):
                out += 5 * ' '
                for j in range(tinggi - i):
                    out += '* '
                out += '\n'
        else:
            bentuk = 'Segitiga Siku-Siku - Siku Bawah '
            # i = 0
            # while i < tinggi:
            #     j = 0
            #     while j <= i:
            #         out += '*'
            #         j+=1
            #     out += '\n'
            #     i += 1
            for i in range(tinggi):
                out += 5 * ' '
                for j in range(i+1):
                    out += '* '
                out += '\n'
        

    elif pil_menu == '2':
        bentuk = 'Segitiga Sama Kaki'

        while val == True:
            tinggi = input('Berapa Tinggi dari Segitiga? (Maksimal 20) ? ')
            if tinggi.isdigit():
                tinggi = int(tinggi)
                if 0 < tinggi < 21:
                    break
                elif tinggi <= 0:
                    print('Tidak boleh 0 atau negatif!')
                else:
                    print('Tidak boleh lebih dari 20!')
            else:
                print('Tidak boleh float atau huruf!')
        
        print('')

        # i = 0
        # k = 1
        # while i < tinggi:
        #     j = 0
        #     out += 2*(2*(tinggi-1)-i) * ' '
        #     while j < k:
        #         out += '* '
        #         j += 1
        #     out += '\n'
        #     i += 1
        #     k += 2 

        k = 1
        for i in range(tinggi):
            out += 2*(2*(tinggi-1)-i) * ' ' 
            for j in range(k):
                out += '* '
            out += '\n'
            k += 2


    elif pil_menu == '3':
        bentuk = 'Persegi'

        while val == True:
            sisi = input('Berapa Sisi dari Persegi? (Maksimal 30) ? ')
            if sisi.isdigit():
                sisi = int(sisi)
                if 0 < sisi < 31:
                    break
                elif sisi <= 0:
                    print('Tidak boleh 0 atau negatif!')
                else:
                    print('Tidak boleh lebih dari 30!')
            else:
                print('Tidak boleh float atau huruf!')
                
        print('')

        for i in range(sisi):
            out += 5 * ' '
            for j in range (sisi):
                out += '* '
            out += '\n'

    else:
        keluar = True
        break

    print(f'Gambar {bentuk}: \n')
    print(out)

    while val == True:
        input_exit = input('Kembali Ke Menu Utama ? (y/n) ')
        if input_exit == 'n' or input_exit == 'y':
            break
        else:
            print('y atau n saja!')
    
    if input_exit == 'n':
        keluar = True
            
print('Terimakasih Sudah Menggunakan Aplikasi Ini!')