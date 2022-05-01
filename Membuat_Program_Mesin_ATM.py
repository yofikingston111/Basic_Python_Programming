user_id = 0
loop = "n"
users =[
    {
        "id": "1234",
        "no_rekening": "1234567890",
        "username": "rijal",
        "pin": "398621",
        "saldo": "100000000"
    },
    {
        "id": "4321",
        "no_rekening": "0987654321",
        "username": "uddin",
        "pin" : "123456",
        "saldo": "45000000",
    }
]
status_login = False
pakai_atm = "y"

def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
        return False

def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return  -1

def cek_rekening(no):
    for  i in range(len(users)):
        if str(users[i]['no_rekening'])==str(no):
            return int(i)
    return -1

def transfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >=0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            users[index2]['saldo'] = users[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp." + str(uang) + "ke rekening " + no_rekening)
            print("sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print('Ops saldo anda tidak cukup')

def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >=0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp." + str(uang))
            print("sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")

while pakai_atm == "y":
    while not status_login:
        print("SELAMAT DATANG DI ATM BANK NEO ECCOMERCE")
        print("Silahkan masukkan pin anda")
        pin = input("Masukkan Pin")

        cl = cek_login(pin)
        if cl:
            print("Selamat Datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")

    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("SELAMAT DATANG DI ATM BANK NEO ECCOMERCE")
        print("1.Cek Saldo")
        print("2.Transfer uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar Atm")
        a = int(input("Silahkan Pilih Menu: "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Transfer Uang Silahkan Masukkan No.Rekening Tujuan")
            no_rekening = input("Masukkan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rekening)

            if cnk >= 0:
                print("Nomor rekening ditemukan, silahkan masukkan nominal yang akan anda transfer")
                nominal = input("Nominal yang akan anda transfer : ")
                transfer_uang(nominal, no_rekening)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Anda Tidak Ditemukan Atau Tidak Terdaftar")
                print("")
                loop = "n"
        elif a == 3:
            nominal = input("Nominal yang akan anda tarik:")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("Pilihan Tidak Tersedia")
        if status_login == True:
            input("Kembali Ke Menu (enter) ")
            print("")
            loop = "y"