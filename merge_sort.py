def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        
        # melakukan pembagian array menjadi dua bagian
        # tergantung dengan nilai midpoint
        left = array[:midpoint]
        right = array[midpoint:]
        
        # memanggil prosedur merge_sort secara 
        # rekursif (bagian divide)
        merge_sort(left)
        merge_sort(right)
        
        # menggabungkan dua bagian array
        i = 0
        j = 0
        k = 0
        
        # membandingkan nilai elemen kedua
        # dalam sebuah elemen, lalu mengurutkan
        # dari nilai terbesar ke terkecil
        while (i < len(left) and j < len(right)):
            if (left[i][1] > right[j][1]):
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        # menggabungkan sisa array left
        while (i < len(left)):
            array[k] = left[i]
            i += 1
            k += 1
        
        # menggabungkan sisa array right
        while (j < len(right)):
            array[k] = right[j]
            j += 1
            k += 1
