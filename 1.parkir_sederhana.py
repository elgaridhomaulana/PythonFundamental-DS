#Konfirmasi Nilai Jam Masuk agar diantara 1-12
check1 = False
while check1 == False:
    jam_masuk = input('Jam Masuk Anda (1-12) ')
    if jam_masuk.isdigit():
        jam_masuk = int(jam_masuk)
        if (jam_masuk > 0) and (jam_masuk < 13):
            check1 = True
        else: 
            print('Inputan Anda hanya bisa 1-12 saja')
    else:
        print('Inputan Anda Salah tidak boleh mengandung huruf')

#Konfirmasi Nilai Waktu Masuk agar hanya bisa am/pm
check2 = False
while check2 == False:
    masuk_waktu = input('Anda Masuk (am/pm) ')
    if (masuk_waktu == 'am') or (masuk_waktu == 'pm'):
        check2 = True
    else:
        print('Anda hanya bisa memasukan waktu masuk antara am atau pm saja')
    

#Konfirmasi Nilai Jam Keluar agar hanya bisa 1-12
check3 = False
while check3 == False:
    jam_keluar = input('Jam Keluar Anda (1-12) ')
    if jam_keluar.isdigit():
        jam_keluar = int(jam_keluar)
        if (jam_keluar > 0) and (jam_keluar < 13):
            check3 = True
        else:
            print('Inputan hanya bisa angka 1-12 saja')
    else:
        print('Inputan Tidak boleh mengandung huruf')

#Konfirmasi Waktu Keluar agar hanya bisa am/pm saja
check4 = False
while check4 == False:
    keluar_waktu = input('Anda Keluar (am/pm) ')
    if (keluar_waktu == 'am') or (keluar_waktu == 'pm'):
        check4 = True
    else:
        print('Anda hanya bisa memasukan waktu keluar antara am atau pm saja')

# Pengubahan waktu PM 
if masuk_waktu == 'pm':
    jam_masuk += 12
    
if keluar_waktu == 'pm':
    jam_keluar += 12

lama_parkir = jam_keluar - jam_masuk

#Penghitungan Lama Waktu Parkir
if (lama_parkir < 0):
    lama_parkir += 24

#Penghitungan Biaya Parkir Berdasarkan Lama Parkir
if lama_parkir == 0:
    biaya = 3000
elif 0 < lama_parkir <= 3:
    biaya = 3000 * lama_parkir
elif lama_parkir > 3:
    biaya_3jam_pertama = 3000 * 3
    biaya = biaya_3jam_pertama + (lama_parkir-3)*1000
    if biaya > 25000 :
        biaya = 25000

print('')
#Menampilkan hasil
print(f'Anda parkir selama {lama_parkir} jam, biaya parkir yang Anda bayar Rp {biaya},-')