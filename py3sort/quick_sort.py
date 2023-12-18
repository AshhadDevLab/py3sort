def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = [x for x in lst[1:] if x >= pivot]
        right = [x for x in lst[1:] if x < pivot]
        pivot_sum = quick_sort(left) + [pivot] + quick_sort(right)
        return pivot_sum[::-1]