def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar angka yang ingin diurutkan secara descending
angka = [42, 19, 33, 8, 55]

# Menggunakan Bubble Sort untuk mengurutkan daftar angka
bubble_sort(angka)

# Menampilkan hasil pengurutan
print("Hasil pengurutan angka secara descending:", angka)
