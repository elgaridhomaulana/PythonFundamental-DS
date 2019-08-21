# Fungsi untuk menghapus huruf vokal dalam sebuah string
def removeVocal(string):
    if 'a' in string:
        string = string.replace('a','')
        if 'i' in string:
            string = string.replace('i','')
            if 'u' in string:
                string = string.replace('u', '')
                if 'e' in string:
                    string = string.replace('e', '')
                    if 'o' in string:
                        string = string.replace('o', '') 
    print(string)
# removeVocal('aiueoj1s*')

# Fungsi check string contain an alphabet
def check(string, alpha_to_check):
    if alpha_to_check.lower() in string.lower():
        print('True') 
    else:
        print('False')
# check('alis', 'A')


# Fungsi untuk mengetahui apakah suatu bilangan ganjil atau genap
def oddEven(number):
    if number % 2 == 0:
        print(f'{number} adalah bilangan genap')
    elif number % 2 == 1:
        print(f'{number} adalah bilangan ganjil')
    else:
        print(f'{number} bukan bilangan ganjil maupun genap')
# oddEven(10)

# Fungsi untuk menghitung nilai terbesar dari 4 angka
def maxNumber(num1, num2, num3, num4):
    num = [num1, num2, num3, num4]
    print(f'bilangan terbesar adalah {max(num)}')
# maxNumber(1,2,3,4)

def stringFilter(string):
    out = ''
    for element in string:
        if element.isdigit():
            out += element
    out = int(out)
    print(out)
# stringFilter('asdfadfa123')

def checkPlatNomor(plat_nomor):
    from datetime import date

    for element in plat_nomor:
        if element.isdigit():
            angka = int(element)
    hari = date.today().day
    if angka % 2 == hari % 2:
        print(f'{plat_nomor} dapat digunakan hari ini, {date.today()}')
    else:
        print(f'{plat_nomor} tidak dapat digunakan hari ini, {date.today()}')
# checkPlatNomor('D 6672 IW')

    
    

    
