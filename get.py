def get_key():
    data = [
        {"User" : "Pengedar", "Kontak" : "0812345678" },
        {"User" : "Donut", "Kontak" : "0912345678" }
    ]
    return data
result = get_key()

for item in result:
    if item.get("User") == "Donut":
        print(item)
    else:
        print("Tidak ada data")