def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Hasil pengurutan:", arr)

#Mengurutkan elemen ascending ke discending.
#membandingkan elemen 1 dengan elemen ke 2, jika lebih besar ditukarkan, begitu seterusnya hingga iterasi terurut dengan benar. dan elemen yang paling besar posisinya akan berada dipaling akhir.