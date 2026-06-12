def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Pass {i + 1}: {arr}")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [100, 99, 54, 22, 1, 29]
bubble_sort(arr)
print("Sorted array:", arr)
