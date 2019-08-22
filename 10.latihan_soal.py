#LATIHAN SOAL
def getSquare(number):
    number = str(number)
    out = ''
    for element in number:
        out += f'{int(element) ** 2}'
    print (out)

# getSquare(121)
# getSquare(553)
# getSquare(44991)

def filterFriend(friends):
    real_friends = [friend for friend in friends if len(friend) == 4]
    print(real_friends)

# filterFriend(['umar','elga','ugha','qwertyuiop'])

def countWords(string):
    y = string.split(' ')
    print(len(y))
    
# countWords('elga pergi ke pasar')

def smallEnough(list, number):
    sum = 0
    for element in list:
        sum += element
    if sum < number:
        print(True)
    else:
        print(False)


# smallEnough([66, 101], 200)
# smallEnough([100,200], 200)

def domainName(url):
    if 'www' in url:
        split_titik = url.split('.') #Return List
        print(split_titik[1])
    else:
        split_slash = url.split('//')
        x = split_slash[1]
        split_titik = x.split('.')
        print(split_titik[0])

# domainName('http://github.com/carbonfive/raygun')
# domainName('http://www.zombie-bites.com')
# domainName('https://www.cnet.com')

def removeDuplicates(string):
    list_string = string.split(' ')
    temp = []
    for element in list_string:
        if element not in temp:
            temp.append(element)
    out = ''
    for item in temp:
        out += f'{item} '
    print(out)

# removeDuplicates('alpha beta beta gamma gamma')

def stringy(number):
    out = ''
    for i in range(number):
        if i % 2 == 0:
            out += '1'
        else:
            out += '0'
    print(int(out))
# stringy(12)  
# stringy(3)
# stringy(4)

def wave(string):
    list1 = []
    for i in range(len(string)):
        out = ''
        for j in range(len(string)):
            if i == j:
                out += string[j].upper()
            else:
                out += string[j]
        list1.append(out) 
    print(list1)

wave('hello')