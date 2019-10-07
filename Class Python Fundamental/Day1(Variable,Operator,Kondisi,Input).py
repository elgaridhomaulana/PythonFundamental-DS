# COMMENT '#'
# Variable adalah wadah untuk menyimpan suatu value

# TIPE DATA PRIMITIF
a = 'Elga' #string
b = 18 #integer
c = True #boolean

# TIPE DATA BUKAN PRIMITIF
d = 18.2 #float
e = [a, b, c, d] #list
f = {'nama': 'elga', 'alamat':'Bandung'} #dictionary

#OPERATOR MATEMATIKA
# + - * / %

angka1 = 15
angka2 = 3
angka3 = '15'
angka4 = '20'

print(angka1 + angka2) # Penjumlahan
print(angka1 - angka2) # Pengurangan
print(angka1 / angka2) # Pembagian
print(angka1 * angka2) # Perkalian
print(angka1 % angka2) # Modulus Operator

print(angka2 * angka3) # '151515'
print(angka1 // angka2) #Floor Division
print(int(angka3) + angka2) #18, angka3 harus diubah menjadi int terlebih dahulu agar dapat ditambahkan

# PENGKONDISIAN

a = 4
b = -6
if a - b == 10:
    print('Good')
    if a > 5:
        print('Great')
    else:
        print('Damn')
else:
    print('Bad')

# if dan elif: akan memilih kondisi yang sesuai pertama kali
c = 7
if c > 4:
    print('Good')
elif c > 6:
    print('Great')
elif c > 9:
    print('Perfect')

# INPUT
inputUser = int(input('Masukan Angka '))
print('Anda memasukan input angka yaitu ' , inputUser)

print(inputUser + 4)
print(inputUser / 4)

#1
year_now = 2019
input_nama = input('Masukan Nama = ')
input_tahun = int(input('Masukan Tahun Lahir = '))
input_pekerjaan = input('Masukan Pekerjaan Anda = ')
print('')
print(f'Nama Anda adalah {input_nama}, Anda berumur {year_now - input_tahun} tahun, Pekerjaan Anda {input_pekerjaan}')


#Kalkulator Sederhana
angka1 = int(input('Masukan Angka Pertama = '))
angka2 = int(input('Masukan Angka Kedua = '))
operator = input('Operator yang dipilih (+, -, *, /) ')

if operator == '+':
    print(angka1 + angka2)
elif operator == '-':
    print(angka1 - angka2)
elif operator == '*':
    print(angka1 * angka2)
elif operator == '/':
    print(angka1 / angka2)
else:
    print('Operator Tidak ada dipilihan')

