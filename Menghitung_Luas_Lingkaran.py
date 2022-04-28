# phi = 3.14
# r = 7
# L = phi * (r * r )
#
# print('Menghitung Luas Lingkaran')
# print('==============================')
# r = int (input('Masukkan jari-jari lingkaran: '))
# phi = 3.14
# L = phi * (r * r )
# print('Luas Lingkaran dengan jari-jari {} adalah {}'.format(r, L))
#

def luas_lingkaran(r):
    return 3.14 * (r * r)

r = input('Masukkan jari-jari lingkaran: ')
luas =  luas_lingkaran(int(r))
print('Luasnya: {}'.format(luas))