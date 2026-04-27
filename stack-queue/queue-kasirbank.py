from collections import deque

queue = deque()

queue.append("Mama Gufron")
queue.append("Gus Ulil")
queue.append("Ngab Owi")
deque(["Mama Gufron", "Gus Ulil", "Ngab Owi"])


def rekening_nasabah():
    nasabah = {
        "Mama Gufron": "Rp. 10.000.000",
        "Gus Ulil": "Rp. 5.000.000",
        "Ngab Owi": "Rp. 2.000.000",
    }
    return nasabah


print("List Antrean :", list(queue))

print("------ Transaksi Dimulai ------")

nomor = 1

while queue:
    nasabah = queue.popleft()
    saldo = rekening_nasabah()[nasabah]
    print(f"{nomor}. {nasabah} dilayani dengan saldo {saldo}")
    nomor += 1
