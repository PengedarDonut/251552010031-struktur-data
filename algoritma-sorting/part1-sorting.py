import matplotlib.pyplot as plt
import pandas as pd

# Data penjualan selama 6 hari pertama (10 baris)

data = [
    {
        "Tanggal": "2026-06-01",
        "Warna": "Merah",
        "Ukuran": "M",
        "Jumlah": 21,
        "Harga": 100000,
    },
    {
        "Tanggal": "2026-06-02",
        "Warna": "Putih",
        "Ukuran": "L",
        "Jumlah": 9,
        "Harga": 100000,
    },
    {
        "Tanggal": "2026-06-03",
        "Warna": "Merah",
        "Ukuran": "L",
        "Jumlah": 7,
        "Harga": 100000,
    },
    {
        "Tanggal": "2026-06-04",
        "Warna": "Hitam",
        "Ukuran": "S",
        "Jumlah": 1,
        "Harga": 100000,
    },
    {
        "Tanggal": "2026-06-05",
        "Warna": "Hitam",
        "Ukuran": "XXXXXL",
        "Jumlah": 10,
        "Harga": 200000,
    },
    {
        "Tanggal": "2026-06-06",
        "Warna": "Hitam",
        "Ukuran": "XL",
        "Jumlah": 1,
        "Harga": 150000,
    },
]

df = pd.DataFrame(data)
df["Total"] = df["Jumlah"] * df["Harga"]

total_penjualan = df["Total"].sum()

warna_order = ["Merah", "Putih", "Hitam"]
warna_terjual = df.groupby("Warna")["Jumlah"].sum().reindex(warna_order)
total_kaos = warna_terjual.sum()

probabilitas = (warna_terjual / total_kaos) * 100

print("Total Penjualan Selama 6 Hari: Rp {:,.0f}".format(total_penjualan))
print("\nProbabilitas Warna Paling Sering Dibeli:")
for warna, prob in probabilitas.items():
    print(f"{warna}: {prob:.2f}%")

warna_grafik = ["red", "white", "black"]
plt.figure(figsize=(8, 5))
plt.bar(probabilitas.index, probabilitas.values, color=warna_grafik, edgecolor="yellow")
plt.title("Probabilitas Pembelian Kaos per Warna Dalam 6 Hari")
plt.ylabel("Persentase (%)")
plt.xlabel("Warna")
plt.ylim(0, 50)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("grafik_probabilitas.png", dpi=100, bbox_inches="tight")
print("Grafik 1 disimpan sebagai 'grafik_probabilitas.png'")
plt.close()

warna_data = list(zip(warna_terjual.index, warna_terjual.values))


def bubble_sort(warna_data):
    n = len(warna_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if warna_data[j][1] < warna_data[j + 1][1]:
                warna_data[j], warna_data[j + 1] = warna_data[j + 1], warna_data[j]
    return warna_data


sorted_data = bubble_sort(warna_data)

print("\nHasil Pengurutan (Bubble Sort) Berdasarkan Jumlah Terbanyak : ")
for warna, jumlah in sorted_data:
    print(f"{warna}: {jumlah} kaos")

plt.figure(figsize=(8, 5))
sorted_warna, sorted_jumlah = zip(*sorted_data)
warna_grafik_sorted = [
    "red" if w == "Merah" else "white" if w == "Putih" else "black"
    for w in sorted_warna
]

plt.bar(sorted_warna, sorted_jumlah, color=warna_grafik_sorted, edgecolor="yellow")
plt.title("Probabilitas Pembelian Kaos per Warna Dalam 6 Hari")
plt.ylabel("Jumlah Kaos")
plt.xlabel("Warna")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("grafik_bubble_sort.png", dpi=100, bbox_inches="tight")
print("Grafik 2 disimpan sebagai 'grafik_bubble_sort.png'")
plt.close()
