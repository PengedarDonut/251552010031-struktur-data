def jump_search(arr, x):
    n = len(arr)
    step = int(n**0.5)  # Calculate the optimal jump size
    prev = 0

    # Jump to the block where the element may be present
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1  # Element not found

    # Perform linear search within the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i  # Element found

    return -1  # Element not found


data = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
cari = int(input("Masukan Angka Yang Ingin Dicari : "))
hasil = jump_search(data, cari)
if hasil != -1:
    print(f"Angka {cari} ditemukan di indeks {hasil}")
else:
    print(f"Angka {cari} tidak ditemukan dalam array")
