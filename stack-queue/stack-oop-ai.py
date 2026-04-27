class StackPiring:
    def __init__(self):
        self.tumpukan = []

    def is_empty(self):
        return len(self.tumpukan) == 0

    # --- FITUR BARU: Menampilkan visual tumpukan agar lebih rapi ---
    def lihat_visual_tumpukan(self):
        """Mencetak kondisi tumpukan piring saat ini ke layar"""
        print("\n[ Kondisi Tumpukan Piring ]")
        if self.is_empty():
            print("  ( Kosong )")
        else:
            # Kita gunakan fungsi reversed() untuk mencetak dari elemen paling atas (terakhir) ke bawah
            for piring in reversed(self.tumpukan):
                print(f"  | {piring} |")
            print("  =============")  # Ini ceritanya meja atau alas tumpukan
        print("-" * 40)  # Garis pembatas agar rapi
        print()  # Tambahan baris kosong

    def push(self, piring):
        self.tumpukan.append(piring)
        print(f"➕ AKSI: Menaruh '{piring}' ke atas tumpukan.")

    def pop(self):
        if self.is_empty():
            print("❌ AKSI GAGAL: Tumpukan piring sudah kosong!")
            return None
        else:
            piring_yang_diambil = self.tumpukan.pop()
            print(f"➖ AKSI: Mengambil '{piring_yang_diambil}' untuk dicuci.")
            return piring_yang_diambil

    def peek(self):
        if self.is_empty():
            print("🔍 INFO: Tumpukan piring kosong.")
            return None
        else:
            piring_teratas = self.tumpukan[-1]
            print(f"🔍 INFO: Mengintip piring paling atas -> '{piring_teratas}'.")
            return piring_teratas

    def size(self):
        jumlah = len(self.tumpukan)
        print(f"📊 INFO: Total ada {jumlah} piring di tumpukan.")
        return jumlah


# ==========================================
# SIMULASI DENGAN OUTPUT YANG LEBIH RAPI
# ==========================================

print("=" * 40)
print("   MEMULAI SIMULASI CUCI PIRING LIFO")
print("=" * 40)

tempat_cucian = StackPiring()

# 1. Menaruh 3 piring secara berurutan
tempat_cucian.push("Piring Kaca Biru")
tempat_cucian.push("Piring Plastik Merah")
tempat_cucian.push("Mangkok Ayam Jago")

# Lihat visual tumpukannya sekarang
tempat_cucian.lihat_visual_tumpukan()

# 2. Cek ukuran dan intip yang paling atas
tempat_cucian.size()
tempat_cucian.peek()

print("\n--- Mulai Mencuci! ---\n")

# 3. Mengambil 1 piring
tempat_cucian.pop()
tempat_cucian.lihat_visual_tumpukan()

# 4. Mengambil 1 piring lagi
tempat_cucian.pop()
tempat_cucian.lihat_visual_tumpukan()

# 5. Mengambil piring terakhir
tempat_cucian.pop()
tempat_cucian.lihat_visual_tumpukan()

# 6. Mencoba mengambil saat sudah kosong
tempat_cucian.pop()
