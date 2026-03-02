def setdefault_dictionary():
    User = {"Pengedar" : "0812345678", "Donut" : "09123456789"}
    return User

data_user = setdefault_dictionary()
data_user.setdefault("Pengedar", "0812345678")
print("Setelah di setdefault : ", data_user)