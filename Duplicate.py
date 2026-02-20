data = [1, 1, 1, 3, 5, 6, 8, 8, 9, 10]
hasil = []

for item in data:
    if item not in hasil:
        hasil.append(item)
       
print(f"Data tanpa Duplikat: {hasil}")