def update_dictionary():
    User = {"Pengedar" : "0812345678", "Donut" : "09123456789"}
    return User

data_user = update_dictionary()
data_user.update({"Enak" : "0712345678"})
print("Setelah di update : ", data_user)
