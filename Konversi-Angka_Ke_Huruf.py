nilai = int(input('masukkan nilai dalam angka 1-100: '))

hasil = None
if nilai <=100 and nilai > 80:
    hasil = 'A'
elif nilai <= 80 and nilai > 60:
    hasil = 'B'
elif nilai <=60 and nilai > 40:
    hasil = 'C'
elif nilai <=40 and nilai > 20:
    hasil = 'D'
elif nilai <=20 and nilai > 0:
    hasil = 'E'
else:
    print('input salah:')

print('Nilai {} = {}'.format(nilai, hasil))