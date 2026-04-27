from collections import deque


class AntreanKasir:
    def __init__(self):
        self.antrean = deque()

    def is_empty(self):
        return len(self.antrean) == 0

    def enqueue(self, pelanggan):
        self.antrean.append(pelanggan)
        print(f"{pelanggan} masuk ke antrean. Antrean: {list(self.antrean)}")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong. Tidak ada pelanggan untuk dilayani.")
            return None
        else:
            yang_dilayani = self.antrean.popleft()
            print(f"{yang_dilayani} dilayani. Antrean: {list(self.antrean)}")
            return yang_dilayani

    def peek(self):
        if self.is_empty():
            print("Antrean kosong. Tidak ada pelanggan untuk dilihat.")
            return None
        else:
            paling_depan = self.antrean[0]
            print(f"Pelanggan paling depan: {paling_depan}")
            return paling_depan

    def liat_antrean(self):
        visual = list(self.antrean)
        print(f"Antrean saat ini: {visual}")


# Simulasi Penggunaan

kasir = AntreanKasir()

kasir.enqueue("Mama Gufron")
kasir.enqueue("Gus Ulil")
kasir.enqueue("Ngab Owi")

kasir.peek()

print("\nMelayani pelanggan:")

kasir.dequeue()
kasir.dequeue()

kasir.peek()
