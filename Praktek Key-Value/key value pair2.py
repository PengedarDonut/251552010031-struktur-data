# Data pengguna
user = {
    "Donut" : "09123456789",
    "Pengedar" : "0812345678"
}
 #daftar username dan password
data_login = [
    ("Donut", "09123456789"),
    ("Pengedar", "0812345678")
]

for username, password in data_login:
    if username in user and user[username] == password:
        print(f"Login berhasil untuk {username}!")
    else:
        print(f"Login gagal untuk {username}! Pastikan username dan password benar.")