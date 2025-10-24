def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


lista_desordenada = [5, 3, 8, 2, 1, 9, 4, 6, 7] 
print('lista desordenada: ', lista_desordenada)
print('lista ordenada: ', insertion_sort(lista_desordenada))
