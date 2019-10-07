# 2D list
produk = [
    ['Jeruk', 10000],
    ['Apel', 30000],
    ['Anggur', 40000]
]

# cart = [
#     [0,3],
#     [1,4],
#     [2,5],
#     [0,5]
# ]
# j = 0
# for i in cart:
#     print(f' {j+1} {produk[i[0]][0]} Rp {produk[i[0]][1]} x {i[1]} = {produk[i[0]][1]*i[1]}')
#     j += 1

# out = '' 
# for i in range(len(cart)):
#     index = cart[i][0]
#     out += f' {i+1}. {produk[index][0]} Rp {produk[index][1]} x {cart[i][1]} = {produk[index][1] * cart[i][1]} \n'
# print(out)

# #DICTIONARY

teh = {
    'teh1' : 'Lavender',
    'teh2' : 'Chamomile',
    'teh3' : 'Lavender',
    'teh4' : 'Green Tea'
}

# for name, variant in teh.items():
#     if variant == 'Chamomile':
#         print(name)

# TUPLE
t = (2, [1, True], {'name': 'elga'})
t[1].append(False)
# print(t)
t[2]['first_name'] = 'maulana'
t[2]['last_name'] = 'elga'
# print(t)

# SETS
list1 = [1,1,1,2,3,4,5,7,1,2, 'A', 'B', 'C']
set1 = set(list1)
# print(set1)
# set2 = {1,2,3,4,4,5,5,6,6,7}
# list1 = list(set2)
# print(list1)

#LIST COMPREHENSION
import random
list_angka = [random.randint(1,3) for i in range(10)]
# print(list_angka)

tahun_lahir = [1990, 1995, 1991, 1989, 1988]
umur = [2019 - tahun for tahun in tahun_lahir]
# print(umur)

bintang = [(i+1)*'*' for i in range(5)]
# print(bintang)

# LAMBDA EXPRESSION
# x = lambda number : number + 5
# print(x(10))

# MAP
def umur_anda(tahun):
    return 2019 - tahun

umur = list(map(lambda a: 2019-a, tahun_lahir))
# print(umur)

# Map sebenarnya menjalankan fungsi seperti dibawah ini
def dupMap(function, object_to_iterate):
    newList = []
    for element in object_to_iterate:
        newList.append(function(element))
    return newList

# print(dupMap(umur_anda, 19))

# FILTER
print(list(filter(lambda tahun: tahun % 2 == 0, tahun_lahir)))

# SEARCHING
numlist = []
