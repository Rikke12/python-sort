def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar nilai ujian siswa Hannah
nilai_hannah = [78, 65, 90, 82, 70]

# Menggunakan Bubble Sort untuk mengurutkan daftar nilai
bubble_sort(nilai_hannah)

# Menampilkan hasil pengurutan
print("Hasil pengurutan nilai Hannah:", nilai_hannah)
