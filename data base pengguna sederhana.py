# Membuat data base sederhana menggunakan input dan dictionary
import email


def data_base():
    data = {}
    jenis = input("Masukkan jenis makanan anda : ")
    harga = input("Masukkan harga makanan anda : ")
    stok = input("Masukkan stok makanan anda : ")
    data[jenis] = {"harga": harga, "stok": stok}
    return data

data_user = data_base()
for key, value in data_user.items():
    print("Jenis makanan : ", key)
    print("Harga makanan : ", value["harga"])
    print("Stok makanan  : ", value["stok"])