from collections import deque

d = deque([1, 2, 3])

print("Angaka Ditambah ", d.append(4), list(d))
print("Angaka Ditambah ", d.appendleft(0), list(d))
print("Angaka Dihapus ", d.pop(), list(d))
print("Angaka Dihapus ", d.popleft(), list(d))

d2 = deque([1, 2, 3, 4, 5])
d2.rotate(2)
print(d2)
d2.rotate(-2)
print(d2)
