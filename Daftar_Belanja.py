#Membuat program daftar belanja

#menambah daftar belanja
def tambah_belanja(text):
    file = open('belanja.txt', 'a+')
    file.write('\n' + text)
#list belanja
def daftar_belanja():
    file = open('belanja.txt', 'a+')
    file.seek(0)
    text = file.read()
    print(text)
#tentang apps
def tentang_program():
    tentang = open('about.txt','r')
    app = tentang.read()
    print(app)

def membaca_daftar_source_code():
    kode = open('source.txt', 'r')
    apps = kode.read()
    print(apps)

def tanya_pengguna():
    print('Silahkan Masukkan Keperluan Belanja anda ke daftar Belanja')
    print('========================DAFTAR BELANJA====================')
    tambah_belanja(input('Mau Belanja Apa: '))

loop = True

print('==============Menu====================')
print('1. Tambah ke Daftar Belanja')
print('2. List Belanja')
print('3. Quit/Keluar')
print('4. About Apps')
print('5. View code')
print('=======================================')
while (loop):
    print('\n')
    menu = input('Masukkan Menu = ')
    if menu == "1":
        tanya_pengguna()
    elif menu == "2":
        daftar_belanja()
    elif menu == "3":
        quit()
    elif menu == "4":
        tentang_program()
    elif menu == "5":
        membaca_daftar_source_code()
    else:
        print("command not found")
