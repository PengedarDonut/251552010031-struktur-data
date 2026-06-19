def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


data = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
cari = int(input("Masukan Angka Yang Ingin Dicari : "))
hasil = binary_search(data, cari)

if hasil != -1:
    print(f"Angka {cari} ditemukan di indeks {hasil}")
else:
    print(f"Angka {cari} tidak ditemukan dalam array")
