#contoh tanpa while
# def run():
#     nama = input('input nama: ')
#     alamat = input('input alamat: ')
#     ttl = input('input tempat tanggal lahir: ')
#     pekerjaan = input('Pekerjaan: ')
#     status = input('Status: ' )
#
#     print('==============================')
#     print('Biodata anda adalah: ')
#     print('nama: ' + nama)
#     print('alamat: ' + alamat)
#     print('ttl: ' + ttl)
#     print('pekerjaan: ' + pekerjaan)
#     print('status: ' + status)

#contoh2
# def get_biodata():
#     nama = input('input nama: ')
#     alamat = input('alamat: ')
#     ttl = input('Tempat tanggal lahir: ')
#     pekerjaan = input('Pekerjaan: ')
#     status = input('status: ')
#     print('==========================')
#     print('Biodata anda adalah: ')
#     print('nama: ' + nama)
#     print('alamat: ' + alamat)
#     print('ttl: ' + ttl)
#     print('pekerjaan: ' + pekerjaan)
#     print('status: ' + status)
#
# def run():
#     while True:
#         get_biodata()
#         input_lagi = input('apakah input lagi? (y/n): ')
#         if input_lagi == 'y':
#             continue
#         elif input_lagi == 'n':
#             break

#contoh3
def get_biodata():
    kebutuhan_data = ['nama', 'alamat', 'ttl', 'pekerjaan', 'status']
    inputan_biodata = []
    for data in kebutuhan_data:
        inputan = input('input {}: '.format(data))
        inputan_biodata.append(inputan)

    print('====================================')
    print('Biodata anda adalah: ')
    for id, hasil in enumerate(inputan_biodata):
        print(kebutuhan_data[id] + ': ' + hasil)

def run():
    while True:
        get_biodata()
        input_lagi = input('apakah input lagi? (y/n): ')
        if input_lagi == 'y':
            continue
        elif input_lagi == 'n':
            break
if __name__ == '__main__':
    run()