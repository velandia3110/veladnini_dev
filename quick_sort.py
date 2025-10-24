def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

lista = [8, 3, 1, 7, 0, 10, 2]
print('lista original:', lista)

lista = quick_sort(lista)
print('lista ordenada:', lista)
