def dupString(string):
    out = ''
    for i in range(len(string)):
        for j in range(i+1):
            out += string[i]
    print(out)
# DupString('arcana')

def dupStringDua(string):
    out = '' 
    for i in range(len(string)):
        for j in range(i+1):
            if j == 0:
                out += string[i].upper()
            else:
                out += string[i]
        
        if i == len(string)-1:
                break
        out += '-'
    print(out)

# dupStringDua('elga')

def Pyramid(tinggi):
    out = ''
    bilangan = 1
    for i in range(tinggi):
        for space in range(3*(tinggi-i)):
            out += ' '
        for angka in range((i*2)+1):
            out += f'{bilangan}'
            if bilangan < 10:
                out += 2* ' '
            elif bilangan > 9 and bilangan < 101:
                out += ' '
            bilangan += 1
        out += '\n'
    print(out)

Pyramid(18)

