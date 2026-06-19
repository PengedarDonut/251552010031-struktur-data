def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


data = list(range(1, 100000))

cari = int(input("Masukan Angka Yang Ingin Dicari : "))
hasil = linear_search(data, cari)

if hasil != -1:
    print(f"Angka {cari} ditemukan di indeks {hasil}")
else:
    print(f"Angka {cari} tidak ditemukan dalam array")
