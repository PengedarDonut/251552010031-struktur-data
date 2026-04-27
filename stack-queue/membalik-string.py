def membalik_string(teks):
    stack = []

    for char in teks:
        stack.append(char)

    hasil = ""

    while stack:
        hasil += stack.pop()

    return hasil


# Contoh penggunaan
kata1 = "Donut"
print(f"Kata asli: {kata1} -> Kata dibalik: {membalik_string(kata1)}")
kata2 = "Kue Cubit"
print(f"Kata asli: {kata2} -> Kata dibalik: {membalik_string(kata2)}")
kata3 = "Kue Lapis"
print(f"Kata asli: {kata3} -> Kata dibalik: {membalik_string(kata3)}")
