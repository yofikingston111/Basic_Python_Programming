# def main():
#     print('Menentukkan Nilai Maksimum dua bilangan')
#
#     #menentukkan input user
#     a = int(input("masukkan bilangan pertama :"))
#     b = int(input("masukkan bilangan kedua :"))
#
#     #Menentukkan Nilai Bilangan dengan if-else
#     if a > b:
#         maks = a
#     else:
#         maks = b
#
#     #mencetak nilai maksimum
#     print('Nilai Terbesar adalah %d'% maks)
#
# if __name__ == '__main__':
#     main()


#develop program 1
# def main():
#     #cetak judul program
#     print('Program Menentukkan Nilai Maksimum Tiga Bilangan Pertama')
#
#
#     #input nilai terbesar
#     a = int(input('masukkan bilangan ke-1: '))
#     b = int(input('masukkan bilangan ke-2: '))
#     c = int(input('masukkan bilangan ke-3: '))
#
#     #menentukkan nilai terbesar
#     if a > b:
#         if a > c:
#             maks = a
#     else:
#         if b > c:
#             maks = b
#         else:
#             maks = c
#     print('Nilai yang terbesar adalah: %d' % maks)
#
# if __name__ == '__main__':
#     main()

#develop program 2
# def main():
#     #cetak judul
#     print('Menentukan nilai 3 bilangan cara kedua: ')
#
#     #input dari user
#     a = int(input('masukkan bilangan ke-1: '))
#     b = int(input('masukkan bilangan ke-2: '))
#     c = int(input('masukkan bilangan ke-3: '))
#
#     #menentukan nilai bilangan
#     if a > b and a > c:
#         maks =a
#     else:
#         if b > a and b > c:
#             maks = b
#         else:
#             maks = c
#     # cetak nilai bilangan
#     print('Bilangan Terbesar adalah: %d' % maks)
#
# if __name__ == '__main__':
#     main()

#develop program 3
# def main():
#     #cetak judul
#     print('Menentukkan nilai 3 bilangan menggunakan cara ketiga')
#
#     #input dari user
#     a = int(input('Masukkan Nilai Ke-1: '))
#     b = int(input('Masukkan Nilai Ke-2: '))
#     c = int(input('Masukkan Nilai Ke-3: '))
#
#     #menentukkan nilai bilangan
#     maks = a
#     if b > maks:
#         maks = b
#     if c > maks:
#         maks = c
#
#     #print result
#     print('Bilangan Terbesar Adalah: %d' % maks)
#
# if __name__ == '__main__':
#     main()

#develop program 4
def main():
    #siapkan list untuk menampung input dari user
    data = []

    #counter(variable hitung/counter)
    count = 'y'

    #logika
    while count == 'y':
        print('Data List Sekarang: ', data)

        bilangan_pertama = int(input('Masukkan angka: '))
        bilangan_kedua = int(input('Masukkan Bilangan Kedua: '))
        data.append(bilangan_pertama)
        data.append(bilangan_kedua)

        #membandingkan nilai dengan fungsi max
        maksimum = max(data)
        print('bilangan maksimumnya adalah: {}'.format(maksimum))

        #input counter
        count = input(('Input data lagi: y/n '))

        if count != 'y':
            print('program selesai')
            break

if __name__ == '__main__':
    main()