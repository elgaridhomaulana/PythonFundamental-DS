# ASSIGNMENT OPERATOR
a = 5
b = a

# b += a ## sama saja dengan b = b + a

# COMPARISON OPERATOR (Mengembalikan Nilai Berupa Boolean)
print(3 > 5)
print(4 == 4)

# LOGICAL OPERATOR
# and, or, not 

# MENGHITUNG INDEKS MASSA TUBUH (BMI)
massa = float(input('Masukan Massa Badan (kg) ? '))
while massa < 0:
    print('Gaboleh Minus massa Anda')
    massa = float(input('Masukan Massa Badan (kg) ? '))

tinggi = float(input('Masukan tinggi Badan (cm) ? '))
tinggi /= 100 # Pengubahan menjadi meter

imt =  massa / (tinggi ** 2)
print(f'Index Massa Tubuh {round(imt, 2)}')
if imt < 18.5:
    print('Berat Badan Anda Kurang')
elif 18.5 <= imt < 25:
    print('Berat Badan Anda Ideal')
elif 25 <= imt < 30:
    print('Berat Badan Anda Berlebih')
elif 30 <= imt < 40:
    print('Berat Badan Anda sangat Berlebih')
else:
    print('Berhati-hati Anda mungkin terkena Obesitas')

# LOOPING
# 1. WHILE LOOP
angka = 1
while angka < 10:
    angka += 1
    print(angka)

# INFINITE LOOP
# angka = 1
# while angka > 0:
#     angka += 1
#     print(angka)

# LOOPING JUMLAH
angka = 1
jumlah = 0
while angka < 5:
    jumlah += angka
    angka += 1
    print(jumlah)

i = 10
out = ''
while i > 0:
    out += str(i)
    if(i == 1):
        break
    out += ', '
    i -= 1
# print(out)

    
