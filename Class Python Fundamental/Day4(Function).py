# FUNCTION

# def namafunction():
#     prog

def contoh():
    print('Hello World')

# FUNCTION WITH PARAMETER
def penjumlahan(a,b):
    x = a+b
    return x

# print(penjumlahan(3,4))

def penjumlahan_4angka(a, b, c, d=1):
    print (a+b+c+d)

# penjumlahan_4angka(1,2,3,4)

def removeChar(string, char_want_to_remove):
    print(string.replace(char_want_to_remove, ''))

# removeChar('elga', 'g')

def suit_jepang(player1, player2):
    print(f'player 1 memilih {player1} dan player 2 memilih {player2}')
    if player1.upper() == player2.upper():
        print('DRAW')
    elif player1.upper() == 'KERTAS':
        if player2.upper() == 'BATU':
            print('player 1 WIN')
        elif player2.upper() == 'GUNTING':
            print('player 1 LOSE')
        else:
            print('player 2 inputannya salah')
    elif player1.upper() == 'GUNTNG':
        if player2.upper() == 'BATU':
            print('player 1 LOSE')
        elif player2.upper() == 'KERTAS':
            print('player 2 WIN')
        else:
            print('player 2 inputannya salah')
    elif player1.upper() == 'BATU':
        if player2.upper() == 'GUNTING':
            print('player 1 LOSE')
        elif player1.upper() == 'KERTAS':
            print('player 1 WIN')
        else:
            print('inputan player 2 salah')
    else:
        print('Masukan Ada yang salah, harus gunting, kertas, batu')

