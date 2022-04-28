#Membuat program kasir resto sederhana
def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
        kasir()

    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()

    else:
        print('input program salah harap ulangi')
def kasir():
    #masukkan input user
    nama_barang = input('masukkan pesanan anda: ')
    harga = int(input('masukkan harga barang: '))
    jumlah_beli = int(input('masukkan jumlah barang yang anda beli: '))

    #menghitung jumlah harga
    total = harga * jumlah_beli

    #cetak total harga
    print(f'harga total: {nama_barang}, = {total}')

    #input pembayaran user
    bayar = int(input('masukkan pembayaran: '))

    #mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total

    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()

    elif bayar == total:
        print('uang anda pas, terimkasih telah berbelanja ')

    else:
        print(f'Maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()

def main_menu():
    #membuat daftar menu pada kasir
    print('=' * 10, 'MAIN MENU APLIKASI KASIR', '=' * 10)
    print('selamat datang di aplikasi kasir')
    print('=' * 20, 'masukkan input aplikasi', '=' * 20)
    print('1. Program Kasir')
    print('2. Program Kalkulator')
    print('3. Exit Program')

    #input pilihan
    pilihan = input('pilihan menu: ')

    #pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('Program Exit')
        exit()

#membuat fungsi authentikasi sederhana
def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukkan username kasir anda: ')
    password = input('masukkan password kasir anda: ')

    if username == 'rijal' and password == '12345':
        print('login berhasil..\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()

def tanya():
    tanya = input('kembali ke menu..? (y/n)' )
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukkan input dengan benar')

#membuat kalkulator
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

    operator = input('masukkan operator: ')

    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('masukkan input yang benar sesuai dengan menu diatas')

#main program
if __name__ == '__main__':
    get_login()

