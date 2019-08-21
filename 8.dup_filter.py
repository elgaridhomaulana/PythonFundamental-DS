def dup_filter(function, givenlist):
    hasil = [number for number in givenlist if function(number) == True]
    return hasil

# list1 = [1,1,1,9,19,20,1,3,4,5,6,7,14,108,109,0,0]
# print(dup_filter(lambda a: a>10, list1))

list2 = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam']
while True:
    search = input(f'{list2} \n Search: ')
    hasil = [element for element in list2 if search.lower() in element.lower() ]
    print(hasil)
    cari_lagi = input('(y) untuk mencari lagi?')
    if cari_lagi != 'y':
        break


