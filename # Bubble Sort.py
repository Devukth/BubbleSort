# Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

array = [4, 6, 2, 5, 7, 1, 3, 8, 10, 9]
print(bubble_sort(array))