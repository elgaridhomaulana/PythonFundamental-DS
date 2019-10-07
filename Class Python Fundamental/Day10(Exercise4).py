def numOfPairs(givenlist):
    dictionary = {}
    for element in givenlist:
        if element in dictionary.keys():
            dictionary[element] += 1
        else:
            dictionary[element] = 1

    pairs = 0
    for value in dictionary.values():
        pairs += (value // 2)
    print(pairs)

def numOfPairs2(givenlist):
    list1 = []
    total_pair = 0
    for element in givenlist:
        list_element = [x for x in givenlist if x == element]
        if element not in list1:
            pair = len(list_element) // 2
            total_pair += pair
        list1.append(element)
    print(total_pair)

def numOfPairs3(givenlist):
    i = 0
    pairs = 0
    while i < len(givenlist):
        j = 1
        cocok = False
        while j < len(givenlist):
            if givenlist[i] == givenlist[j]:
                pairs += 1
                givenlist.pop(j)
                givenlist.pop(i)
                cocok = True
                break
            j += 1
        if cocok:
            i = 0
        else:
            givenlist.pop(i)
            i = 0
    print(pairs)

# numOfPairs3(['red', 'red', 'green', 'green', 'green', 'blue', 'blue'])

def findUniq(givenlist):
    dictionary = {}
    for element in givenlist:
        if element in dictionary.keys():
            dictionary[element] += 1
        else:
            dictionary[element] = 1
    list_uniq = []
    for key,value in dictionary.items():
        if value == 1:
            list_uniq.append(key)
    hasil = 'Nilai yang unik adalah '
    for i in range(len(list_uniq)):
        if i == (len(list_uniq) - 1):
            hasil += f'dan {list_uniq[i]}.'
        else:
            hasil += f'{list_uniq[i]}, '

    print(hasil)

# findUniq([1,1,1,2,1,1,3,6,9])

def sumofTwoSmallest(givenlist):
    givenlist.sort()
    hasil = givenlist[0] + givenlist[1]
    print(hasil)

# sumofTwoSmallest([100, 80, 70, 50, 5, 2])
a = 3
b = 5
x = a if a > b else b
print(x)


        



