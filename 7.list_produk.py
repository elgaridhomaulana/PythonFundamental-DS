products = ['Green Tea', 'Genmaicha', 'Chamomile']
prices = [80000, 150000, 200000]

def print_list_products():
    print(show_products())
def show_products():
    out = ''
    for i in range(len(products)):
        out += f'{i+1}.  {products[i]} Rp {prices[i]}'
        if i == len(products) - 1:
            break
        out += '\n'
    return out

def add_product():
    product = input('Produk yang mau ditambahkan = ')
    price = input(f'Harga produk {product} = ')
    products.append(product)
    prices.append(price)
    print(f'Product {product} telah berhasil ditambahkan \n {show_products()}')

def update_price():
    num_product_edited = int(input(f'{show_products()} \n Nomor Produk yang harganya mau di edit = '))
    new_price = input(f'Harga {products[num_product_edited-1]} berubah menjadi = ')
    prices[num_product_edited-1] = new_price
    print(f'Harga {products[num_product_edited-1]} telah berhasil diubah \n {show_products()}')

def del_product():
    num_product_deleted = int(input(f'{show_products()} \n Nomor Produk yang mau di delete = '))
    products.pop(num_product_deleted-1)
    prices.pop(num_product_deleted-1)
    print(f'Produk telah berhasil dihapus \n {show_products()}')

while True:

    pil_menu = int(input('MENU UTAMA 1. List Produk 2. Tambah Produk 3. Edit Harga 4. Hapus Produk '))
    menu = [print_list_products, add_product, update_price, del_product]
    menu[pil_menu-1]()

    exit_choice = input('Kembali ke Menu Utama? (y/n)')
    if exit_choice != 'y':
        break
        