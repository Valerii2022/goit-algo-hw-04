import timeit
import random

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Вбудований Timsort
def timsort(arr):
    return sorted(arr)

def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

# Розміри наборів даних
sizes = [1000, 5000, 10000]

# Тестування алгоритмів
for size in sizes:
    data = generate_random_list(size)
    
    # Копії даних для тестування
    data_for_insertion = data[:]
    data_for_merge = data[:]
    data_for_timsort = data[:]
    
    # Вимірювання часу для сортування вставками
    insertion_time = timeit.timeit(lambda: insertion_sort(data_for_insertion), number=1)
    
    # Вимірювання часу для сортування злиттям
    merge_time = timeit.timeit(lambda: merge_sort(data_for_merge), number=1)
    
    # Вимірювання часу для Timsort
    timsort_time = timeit.timeit(lambda: timsort(data_for_timsort), number=1)
    
    print(f"Розмір набору даних: {size}")
    print(f"Сортування вставками: {insertion_time:.6f} секунд")
    print(f"Сортування злиттям: {merge_time:.6f} секунд")
    print(f"Timsort: {timsort_time:.6f} секунд")
    print("-" * 40)