#Memahami Function
# def x():
#     return {'nama' : lambda : lambda : [0, 1, lambda a, b : print(a + b)]}

# x()['nama']()()[2](2,2)

# def tickets(peopleInline):
#     count25, count50, count100 = 0, 0, 0
#     for element in peopleInline:
#         if element == 25:
#             count25 += 1
#         elif element == 50:
#             count50 += 1
#             count25 -= 1
#         else:
#             count100 += 1
#             count25 -= 1
#             if count50 > 1:
#                 count50 -= 1
#             else:
#                 count25 -= 2
    
#     if count25 < 0 or count50 < 0:
#         print('NO')
#     else:
#         print('YES')

def alphasum(string):
    out = ''
    sum = 0
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(string)):
        index = alpha.index(string[i]) + 1
        if i == (len(string) - 1):
            out += f'{index}'
        else:
            out += f'{index} + '
        sum += index
    print(f'{out} = {sum}')

# alphasum('abc')

def alphaNext(string, geser):
    out = ''
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    for element in string:
        index = alpha.index(element)
        if (index + geser) >= len(alpha):
            index = (index + geser) - len(alpha)
            out += f'{alpha[index]}'
        else:
            out += f'{alpha[index + geser]}'
    print(out)

# alphaNext('xyz',2)

def numOfPair(givenlist):
    amount_of_pair = 0
    list1 = []
    for element in givenlist:
        if element not in list1:
            list_element = [x for x in givenlist if x == element]
            element_pair = len(list_element) // 2
            amount_of_pair += element_pair
            list1.append(element)
    print(amount_of_pair)
# numOfPair(['red', 'green', 'red', 'blue', 'blue', 'blue','blue'])


def sumOdd(givenlist):
    total = 0
    for element in givenlist:
        if element % 2 != 0:
            total += element
    print(total)

# sumOdd([3,3,2,2,6,5])
# sumOdd([1,3,2,1,8,5])

def generateNum(givenlist):
    dictionary = {'Jan': 1 , 'Feb': 2 , 'Mar': 3 , 'Apr': 4 , 'May': 5 , 'Jun': 6 , 'Jul': 7 , 'Aug': 8 , 'Sep': 9 , 'Oct': 10, 'Nov': 11, 'Dec': 12}
    out = ''
    #Get Gender
    out += givenlist[3]

    #Get The first letter of First Name
    out += givenlist[0][0]
    #Get the first letter of Last Name
    out += givenlist[1][0]

    #Get the middle letter of Last Name
    if len(givenlist[1]) % 2 != 0:
        out += givenlist[1][len(givenlist)//2].upper()
    else:
        floor_len = len(givenlist)//2
        out += givenlist[1][(floor_len-1):(floor_len+1)].upper()
    
    # Adding Strip
    out += '-'

    # Initialize list of date
    date_list = givenlist[2].split('-')

    # take the last number of date
    out+= date_list[0][-1]
    # take month and change it to number using dictionary(Jan = 1)
    out+= str(dictionary[date_list[1]])
    # take the last two number of the year
    out+= date_list[2][-2:]
    print(out)

generateNum(['John', 'Smith', '01-Jan-1967', 'M'])
# generateNum(['Steve', 'Jobs', '23-Jan-2010', 'M'])

def findUniq(givenlist):
    unique = []
    for element in givenlist:
        list_number = [x for x in givenlist if x == element]
        if len(list_number) == 1:
            unique.append(element)
    if len(unique) == 0:
        print('Nothing')
    else:
        print(unique)
# findUniq([1,1,1,2,1,1])
# findUniq([1,2,1,2,1,1])
# findUniq([0,0,0.55,0,0,0])

def sumTwoSmallest(givenlist):
    total = 0
    two_min_number = []
    for element in givenlist:
        if len(two_min_number) < 2:
            two_min_number.append(element)
        else:
            if element < two_min_number[0]:
                two_min_number[0] = element
            elif two_min_number[0] < element < two_min_number[1]:
                two_min_number[1] = element
    
    if len(two_min_number) < 2:
        print('List harus lebih dari dua angka')
    else:
        for item in two_min_number:
            total += item
        print(total)

# sumTwoSmallest([19, 5, 42, 2, 77])
# sumTwoSmallest([19])




