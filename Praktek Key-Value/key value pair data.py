# Data pengguna
user = {
    "Donut" : "09123456789",
    "Pengedar" : "0812345678"
}

print("===== Login =====")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username in user and user[input_username] == input_password:
    print("Login berhasil!")
else:
    print("Login gagal! Pastikan username dan password benar.")