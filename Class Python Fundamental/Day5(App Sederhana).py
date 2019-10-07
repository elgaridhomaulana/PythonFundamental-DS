products = ['Green Tea', 'Genmaicha', 'Chamomile']
prices = [80000, 150000, 200000]

def tampilkan_produk():
    out = ''
    for i in range(len(products)):
        out += f'{i+1}.  {products[i]} Rp {prices[i]}'
        if i == len(products) - 1:
            break
        out += '\n'
    return out

keluar = False
while keluar == False:
    print('APLIKASI INTERAKTIF')
    menu = input('MENU UTAMA 1. List Produk 2. Tambah Produk 3. Edit Harga 4. Hapus Produk ')

    if menu == '1':
        print(tampilkan_produk())
    elif menu == '2':
        product = input('Produk yang mau ditambahkan = ')
        price = input(f'Harga produk {product} = ')
        products.append(product)
        prices.append(price)
        # tampilkan_produk()
    elif menu == '3':
        print(tampilkan_produk())
        num_product_edited = int(input('Nomor Produk yang harganya mau di edit = '))
        new_price = input(f'Harga {products[num_product_edited-1]} berubah menjadi = ')
        prices[num_product_edited-1] = new_price
        # tampilkan_produk()
    elif menu == '4':
        print(tampilkan_produk())
        num_product_deleted = int(input('Nomor Produk yang mau di delete = '))
        products.pop(num_product_deleted-1)
        prices.pop(num_product_deleted-1)
        # tampilkan_produk()

    back_to_home = input('Mau kembali ke menu awal ? (y/n) ')
    if back_to_home == 'n':
        keluar = True