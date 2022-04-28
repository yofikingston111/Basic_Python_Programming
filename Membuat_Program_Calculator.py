def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukkan username kasir anda: ')
    password = input('masukkan password kasir anda: ')

    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()

def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
        kasir()
    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()
    else:
        print('input program salah harap ulangi')

#create apps caser
def kasir():
    nama_barang = input('Masukkan pesanan anda: ')
    harga = int(input('Masukkan harga barang: '))
    jumlah_beli = int(input('Masukkan jumlah barang yang dibeli: '))

    #menghitung jumlah harga
    total = harga * jumlah_beli

    #cetak total harga
    print(f'harga total: {nama_barang}, = {total}')


    #input pembayaran dari user
    bayar = int(input('masukkan pembayaran: '))

    #mengecek apakah pembayaran kurang atau ada dikembalikan
    kurang = total - bayar
    kembalian = bayar - total

    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()

#create calculator
def kalkulator():
    print('=' * 10)
    print('Program Kalkulator')

    print()
    print('Operator')
    print('=' * 10)
    print('1. tambah')
    print('2. kurang')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi/modulus')

    a = int(input('masukkan bilangan pertama: '))
    b = int(input('masukkan bilangan kedua: '))

    operator = input('masukkan operator')

    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} * {} adalah {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} / {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {}'.format(a, b, a % b ))
    else:
        print('masukkan input yang benar sesuai menu diatas')

#create main menu
def main_menu():
    #create list menu at the caseer
    print('=' * 10, 'MAIN MENU APLIKASI KASIR', '=' * 10)
    print('selamat datang di aplikasi kasir')
    print('=' * 20, 'masukkan input aplikasi', '=' * 20)
    print('1. Program kasir')
    print('2. Program Kalkulator')
    print('3.Exit Program')

    #input pilihan
    pilihan = input('Pilihan Menu: ')

    #pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('Program exit')
        exit()

def tanya():
    tanya = input('kembali ke menu.. ? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukkan input dengan benar')