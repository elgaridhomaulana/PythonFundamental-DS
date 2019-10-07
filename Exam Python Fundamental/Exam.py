def countVowel(string):
    vowel = list('aiueo')
    countVowel = 0
    for element in string:
        if element.lower() in vowel:
            countVowel += 1
    print(countVowel)

# countVowel('budi pergi ke pasar')
# countVowel('purwadhika')

def countWords(string):
    list_string = string.split(' ')
    list1 = []
    for element in list_string:
        if element not in list1:
            x = [item for item in list_string if item == element]
            list1.append(element)
            print(f"Jumlah kata '{element[0].upper()}{element[1:]}' ada sebanyak {len(x)} ")

# countWords('jangan jangan kamu adalah aku')

def given(givenlist):
    hasil = []
    for i in range(len(givenlist)):
        for element in givenlist[i]:
            hasil.append(element)
    hasil.sort()
    print(hasil)

# given([[3,2,1], [4,6,5], [], [9,7,8]])
# given([[3,4,2,1], [1,2,3], [5,4,3,1]])

def remove_outlier(data):
    #sorting data
    sort_data = data.copy()
    sort_data.sort()

    # Finding median, setengah_data_pertama, q1, setengah_data_terakhir, and q3
    median_of_ganjil = lambda values: values[len(values)//2]
    median_of_genap = lambda values : (values[len(values)//2] + values[len(values)//2 -1])/2 

    if len(sort_data) %2 != 0:
        median = median_of_ganjil(sort_data) 
        setengah_data_terakhir = sort_data[(len(sort_data)//2 + 1) :]
        
    else:
        median = median_of_genap(sort_data)
        setengah_data_terakhir = sort_data[(len(sort_data)//2):]

    setengah_data_pertama = sort_data[:len(sort_data)//2]

    q1 = median_of_ganjil(setengah_data_pertama) if len(setengah_data_pertama) % 2 != 0 else median_of_genap(setengah_data_pertama)
    q3 = median_of_ganjil(setengah_data_terakhir) if len(setengah_data_terakhir) % 2 != 0 else median_of_genap(setengah_data_terakhir)

    # Calculating IQR
    IQR = q3 - q1

    # Calculating lower limit and upper limit
    lower_limit = q1 - (1.5*IQR)
    upper_limit = q3 + (1.5*IQR)

    # Making list without outlier using list comprehension
    data_tanpa_outlier = [item for item in data if (item > lower_limit) and (item < upper_limit)]

    #Output of the program
    print(f'data asli = {data}')
    print(f'data setelah di sort = {sort_data}')
    print(f'setengah data pertama = {setengah_data_pertama}')
    print(f'setengah data terakhir = {setengah_data_terakhir}')
    print(f'q1 adalah = {q1}')
    print(f'q3 adalah = {q3}')
    print(f'lower limit adalah = {lower_limit}')
    print(f'upper limit adalah = {upper_limit}')
    print(f'data awal tanpa outlier = {data_tanpa_outlier}')

# data = [70,71,70,73,70,70,69,70,72,71,300,71,69,70] 
# remove_outlier(data)
# data2 = [60,63,64,62,69,80,1,60,63,64,60]
# remove_outlier(data2)
