total = 50000
setelah_diskon = total

if total <100000:
    diskon = total * (5/100)
else:
    diskon = total * (10/100)

setelah_diskon = total - diskon
print('diskonnya yaitu : {}'.format(int(diskon)))
print('Harga setelah diskon : {}'.format(int(setelah_diskon)))

total = int(input('Masukkan total belanja: '))
setelah_diskon = total

if total < 100000:
    diskon = total * (5/100)
else:
    diskon = total * (10/100)

setelah_diskon = total - diskon
print("Diskonnya yaitu: Rp {:,}".format(int(diskon)).replace(',','.'))
print(("Harga setelah diskon: Rp {:,}".format(int(setelah_diskon)).replace(',','.')))
