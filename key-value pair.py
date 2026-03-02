# Key-Pair menggunakan input

from numpy import rint


def keypair_dictionary():
    User = {}
    key = input("Masukkan nama anda    : ")
    value = input("Masukkan email anda : ")
    User[key] = value
    return User

data_user = keypair_dictionary()
for key, value in data_user.items():
    print("Nama user  : ", key)
    print("Nama email : ", value)