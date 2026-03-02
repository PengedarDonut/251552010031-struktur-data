def pop_dictionary():
    User = {"Pengedar" : "0812345678", "Donut" : "09123456789"}
    return User
data_user = pop_dictionary()
hapus = data_user.pop("Pengedar")
print("Setelah di hapus : ", data_user)