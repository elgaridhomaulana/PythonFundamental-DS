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