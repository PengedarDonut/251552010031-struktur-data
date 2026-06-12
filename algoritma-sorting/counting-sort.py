def counting_sort(arr):
    print("Input : ", arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    print("Frekuensi (count array): ")
    for i, c in enumerate(count):
        if c > 0:
            print(f"Angka {i}: {c} kali")

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    print("Output (terurut):", sorted_arr)
    return sorted_arr


data = [1, 5, 2, 9, 7]
counting_sort(data)
