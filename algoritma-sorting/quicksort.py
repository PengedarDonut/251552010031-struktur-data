def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    print(f"Pivot: {pivot}, Less: {less}, Greater: {greater}")
    return quicksort(less) + [pivot] + quicksort(greater)


arr = [10, 2, 1, 4, 5, 99]
sorted_arr = quicksort(arr)
print("Sorted array : ", sorted_arr)
