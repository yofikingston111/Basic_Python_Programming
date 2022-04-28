umur = input("Masukkan umur: ")
if int(umur) <10:
        keterangan = 'Anak-anak'
elif int(umur)<20:
        keterangan = 'Remaja'
elif int(umur)<40:
        keterangan = 'Dewasa'
elif int(umur)<50:
        keterangan = 'Sudah tua'
elif int(umur)<60:
        keterangan = 'Manula'
else:
    keterangan = 'Belum manula'

print('Anda memasukkan umur {}, artinya {}'.format(umur, keterangan))
