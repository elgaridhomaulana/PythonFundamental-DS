dictionary = {}

def print_dict():
    print(show_dict(dictionary))

def show_dict(name_dict):
    out = '\t---------------------------- \n'
    out += "\t {0:20} {1}\n".format('Key','Values')
    out += '\t---------------------------- \n'
    for  key,value in name_dict.items():
        out += "\t {0:20} {1}\n".format(key,value)
    return out

def add_dict():
    jumlah = int(input('Jumlah yang mau ditambah = '))
    for i in range(jumlah):
        tipe_data = int(input('1. String \n2. Number\n Pilihan tipe data = '))
        key_tambah = input('Keys yang mau ditambah = ')
        if tipe_data == 1:
            value_tambah = input(f'Masukan Value dari {key_tambah} = ')
            dictionary[f"'{key_tambah}'"] = f"'{value_tambah}'"
        else:
            value_tambah = int(input(f'Masukan Value dari {key_tambah} = '))
            dictionary[f"'{key_tambah}'"] = value_tambah
    show_dict(dictionary)

def search_dict():
    search = input('Pencarian di Dictionary = ')
    hasil = [element for element in dictionary.keys() if search.lower() in element.lower()]
    temp = {}
    for item in hasil:
        temp[item] = dictionary[item]
    print(show_dict(temp))

def quits():
    exit()

while True:
    pil_user = int(input('Main Menu \n 1. Lihat Full Dictionary\n 2. Menambah Dictionary\n 3. Mencari Dictionary\n 4. Exit\nMasukan Pilihan: '))
    menu = [print_dict, add_dict, search_dict, quits]
    menu[pil_user - 1]()
    pil_exit = input('(y) untuk Kembali ke menu utama? ')
    if pil_exit != 'y':
        break


