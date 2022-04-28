uang = int(input('Masukkan jumlah uang: '))
uang_pecahan = [100000, 50000, 20000,10000, 5000, 2000, 1000, 500, 200]
jumlah_pecahan = {}
sisa = uang
print('Input uang {}, Pecahan yang dibutuhkan yaitu: '.format(uang))
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - (pecahan * banyak_pecahan)
    print('pecahan {} : {}'.format(pecahan, banyak_pecahan))

