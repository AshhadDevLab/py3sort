def heap_sort(lst):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and lst[left] > lst[largest]:
            largest = left

        if right < n and lst[right] > lst[largest]:
            largest = right

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(n, largest)

    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(i, 0)
    return lst