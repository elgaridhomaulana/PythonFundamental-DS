
def capitalize(string):
    ganjil_besar = ''
    genap_besar = ''
    for i in range(len(string)):
        if i % 2 == 0:
            genap_besar += string[i].upper()
            ganjil_besar += string[i]
        else:
            genap_besar += string[i]
            ganjil_besar += string[i].upper()
    print([genap_besar, ganjil_besar])

# capitalize('abcdef')

def reverseWords(string):
    out = ''
    for i in range(len(string)):
        out += string[-1 - i]
    print(out)

# reverseWords('budi pergi ke pasar')


def sortString(string, string2):
    out = ''
    for element in string2:
        for i in range(len(string)):
            if element == string[i]:
                out += element
    out2 = ''
    for element in string:
        if element not in string2:
            out2+= element
    
    print(out+out2)

# sortString('banana', 'an')
 
def like(givenlist):
    if len(givenlist) == 0:
        print('No one likes this')
    else:
        if len(givenlist) == 1:
            print(f'{givenlist[0]} likes this')
        elif len(givenlist) == 2:
            print(f'{givenlist[0]} and {givenlist[1]} like this')
        elif len(givenlist) == 3:
            print(f'{givenlist[0]}, {givenlist[1]}, and {givenlist[2]} like this')
        else:
            print(f'{givenlist[0]}, {givenlist[1]}, and {len(givenlist) - 2} others  like this')

# like(['Elga', 'Umar', 'Ugha', 'Izi'])

def nb_year(p0, percent, aug, p):
    percent = percent/100
    year = 0
    while True:
        p0 = p0*(1+percent) + aug
        year += 1
        if p0 >= p:
            break
    print(year)

# nb_year(1500, 5, 100, 5000)
# nb_year(1500000, 2.5, 10000, 2000000)

def tickets(list):
    count25 = 0
    count50 = 0
    for element in list:
        if element == 25:
            count25 += 1
            check = True
        elif element == 50:
            if count25 >= 1:
                count25 -= 1
                check = True
                count50 += 1
            else:
                check = False
        else:
            if count25 >= 3:
                count25 -= 3
                check = True
            elif count25 >= 1 and count50 >= 1:
                count25 -= 1
                count50 -= 1
                check = True
            else:
                check = False
    if check:
        print('YES')
    else:
        print('NO')

# tickets([25, 25, 50])
# tickets([25, 100])
# tickets([25, 25, 50, 50, 100])
# tickets([25,25,50,100])
# tickets([25,25,25,100])

def rowSumOddNumbers(n):
    out = ''
    out2 = ''
    sum = 0
    k = 1
    for i in range(n):
        out += 3*((n-1)-i) * ' '
        for j in range(i + 1):
            out += f'{k}'
            if i == n-1:
                if j == i:
                    out2 += f'{k}'     
                else:
                    out2 += f'{k} + '
                sum += k
            if k < 10:
                out += ' ' * 5
            elif k > 10 and k < 100:
                out += ' ' * 4
            elif k > 100:
                out += ' ' * 3
            k += 2
        if i != n-1:
            out += '\n'
    out2 += f' = {sum}'
    
    print(out)
    print(out2)
rowSumOddNumbers(4) 

#       1
#    3     5
# 7     9    11