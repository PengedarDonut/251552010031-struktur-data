def function_bubble():
    angka = [2, 3, 6, 8, 10]
    return angka
 
angka = function_bubble()
for i in range(len(angka)):
    for j in range(len(angka)-i-1):
        if angka [j] > angka [j+1]:
            angka [j], angka [j+1], angka [j]
            
print(f"Hasil Sorting: {angka}")