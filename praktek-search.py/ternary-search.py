def ternary_search(arr, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)

    return -1


data = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
cari = int(input("Masukan Angka Yang Ingin Dicari : "))
hasil = ternary_search(data, 0, len(data) - 1, cari)
if hasil != -1:
    print(f"Angka {cari} ditemukan di indeks {hasil}")
else:
    print(f"Angka {cari} tidak ditemukan dalam array")
