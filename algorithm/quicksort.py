def pythonic_quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[-1]
    pivots = [i for i in a if i == pivot]
    left = pythonic_quick_sort([i for i in a if i < pivot])
    right = pythonic_quick_sort([i for i in a if i > pivot])
    return left + pivots + right
