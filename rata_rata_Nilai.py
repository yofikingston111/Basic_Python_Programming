daftar_input = input('Masukkan list bilangan, pisahkan dengan tanda koma. contoh 1, 2, 3 dst: ')
list_angka = daftar_input.split(',')
daftar_baru = [int(x) for x in list_angka]

jumlah = 0
for angka in daftar_baru:
    jumlah += angka
rata_rata  = jumlah / len(daftar_baru)

print('Nilai rata-rata: {}'.format(rata_rata))
print('Jumlah total: {}'.format(jumlah))
print('Nilai Maximal inputan: {}'.format(max(daftar_baru)))
print('Nilai Minimal inputan: {}'.format(min(daftar_baru)))

