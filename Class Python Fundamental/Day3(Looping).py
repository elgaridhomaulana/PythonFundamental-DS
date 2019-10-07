# FOR LOOP
for element in range(100, 50, -10):
    print(element)

# NESTED LOOP

for element1 in range(10):
    for element2 in range(10):
        print(f'{element1},{element2}')
out = ''
for i in range(10):
    for j in range(5):
        out += f'belajar membaca {i} {j}    '
    out+= '\n \n'
# print(out)

i=0
j=0
out = ''
sisi = int(input('Mau berapa kali berapa? '))
while i < sisi:
    j = 0
    while j < sisi:
        out += '*    '
        j +=1
    if i == (sisi-1):
        break
    out += '\n \n'
    i += 1
# print(out)

i = 1
out = ''
while i < 5:
    j = 1
    while j < 5:
        out += f'{j}'
        j +=1
    out += '\n'
    i += 1
# print(out)


out=''
for i in range(1,5):
    for j in range(1,5): 
        out += str(j)
    out+='\n'   
# print(out)

out = ''
for i in range(5):
    for j in range(i):
        j += 1
        out += f'{j}'
    out += '\n'
# print(out)

out = ''
i = 0
while i < 4:
    j = 0
    while j <= i:
        out += f'{j+1}'
        j += 1
    out += '\n'
    i += 1
# print(out)

out = ''
for i in range(5):
    for j in range(i+1):
        out += '*'
    out+= '\n'
# print(out)

i = 0
out = ''
while i < 5:
    j = 0
    while j <= i:
        out += '*'
        j+=1
    out += '\n'
    i+=1
# print(out)

# SEGITIGA TERBALIK
i = 0
out = ''

while i < 5:
    j = 0
    out += i * ' '
    while j < (5-i):
        out += '*'
        j+=1
    out += '\n'
    i+=1

i = 1
while i < 5:
    j = 0
    while j <= i:
        out += '*'
        j+=1
    if i == 4:
        break
    out += '\n'
    i+=1
# print(out)

i = 0
out = ''
k = 1
while i < 5:
    j = 0
    while j < (5-i):
        if k < 10:
            out += str(k) + '  '
        else:
            out += str(k) + ' '
        j+=1
        k+=2
    out += '\n'
    i+=1
# print(out)