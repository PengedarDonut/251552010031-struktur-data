def copy_dictionary():
    data = {"Pengedar" : "08123456789", "Donat" : "0912345678"}
    return data

data_user = copy_dictionary()
copy_data = data_user.copy()
print("Setelah di copy : ", copy_data)
