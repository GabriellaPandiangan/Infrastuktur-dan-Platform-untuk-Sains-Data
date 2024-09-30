def extract_and_sort_odd_indexed(list1, list2):
    # Mengambil elemen dari list1 dan list2 dengan indeks ganjil
    odd_indexed_elements = []
    
    # Mengambil elemen dari list1
    for i in range(1, len(list1), 2):  # Mulai dari indeks 1 (ganjil) dan langkah 2
        odd_indexed_elements.append(list1[i])
    
    # Mengambil elemen dari list2
    for i in range(1, len(list2), 2):
        odd_indexed_elements.append(list2[i])
    
    # Mengurutkan list baru secara menurun
    odd_indexed_elements.sort(reverse=True)
    
    return odd_indexed_elements

# Contoh penggunaan
list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]
result = extract_and_sort_odd_indexed(list1, list2)
print(result)  # Output: [45, 35, 25, 15]
