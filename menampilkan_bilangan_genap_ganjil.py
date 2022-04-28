bil_awal = int(input('Masukkan bilangan awal: '))
bila_akhir = int(input('Masukkan bilangan akhir: '))

list_bil = [i for i in range(bil_awal, bila_akhir +1)]
print('Daftar Bilangan: {}'.format(list_bil))

bil_genap = []
bil_ganjil = []

for bil in list_bil:
    if bil % 2 == 0:
        bil_genap.append(bil)
    else:
        bil_ganjil.append(bil)

print('genap: {}'.format(', '.join([str(bil)for bil in bil_genap])))
print('ganjil: {}'.format(', '.join([str(bil)for bil in bil_ganjil])))