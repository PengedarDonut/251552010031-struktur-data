def popitems_dictionary():
    User = {"Pengedar" : "0812345678", "Donut" : "09123456789"}
    return User

data_user = popitems_dictionary()
hapus = data_user.popitem()
print("Setelah di hapus : ", data_user)