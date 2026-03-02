def clear_dictionary():
    data = {"Pengedar" : "08123456789", "Donat" : "0912345678"}
    return data

data_user = clear_dictionary()
#Sebelum menggunakan clear
print("Sebelum di clear : ", data_user)

#Setelah menggunakan clear
print("Setelah di clear : ", data_user.clear())