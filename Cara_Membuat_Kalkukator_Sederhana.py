def tambah(x, y):
    return x + y
def kurang(x, y):
    return x-y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y

while True:
    print('Menu operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Tutup')
    operasi = int(input('silahkan masukkan operasi pilihan (dalam angka): '))


    if operasi == 1:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print('Hasilnya: {}'.format(tambah(x, y)))
    elif operasi ==2:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print('Hasilnya: {}'.format(kurang(x, y)))
    elif operasi == 3:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print('Hasilnya: {}'.format(kali(x, y)))
    elif operasi == 4:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print('Hasilnya: {}'.format(bagi(x, y)))
    elif operasi == 5:
        print('OPERASI TIDAK DIKENALI \n')
        break





