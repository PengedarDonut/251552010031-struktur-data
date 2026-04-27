from collections import deque

queue = deque()

queue.append("Mama Gufron")
queue.append("Gus Ulil")
queue.append("Ngab Owi")

front = queue[0]
print(f"Si Paling Cepat : {front}")

keluar = queue.popleft()
print(f"{keluar} : Minggat Pertama")

print("Ada sisa berapa makhluk?")
if len(queue) > 0:
    print("Masih ada nih :", len(queue))
else:
    print("Koshong mas!")

print("Sisa siapa aja?")
for i, makhluk in enumerate(queue):
    print(f"{i + 1}. {makhluk}")
