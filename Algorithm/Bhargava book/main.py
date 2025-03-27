import random
import time

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        less = [x for x in lst if x < pivot]
        equal = [x for x in lst if x == pivot]
        more = [x for x in lst if x > pivot]
        return quicksort(less) + equal + quicksort(more)

def merge_sort(lst):
    def sort(lst_a, lst_b):
        new_lst = []
        while len(lst_a) >= 1 and len(lst_b) >= 1:
            if lst_a[0] <= lst_b[0]:
                new_lst.append(lst_a[0])
                lst_a.pop(0)
            else:
                new_lst.append(lst_b[0])
                lst_b.pop(0)
        
        if len(lst_a) > 0:
            return new_lst + lst_a
        else:
            return new_lst + lst_b

    lst_size = len(lst)
    if lst_size == 1:
        return lst
    else:
        lst_a = lst[: lst_size//2]
        lst_b = lst[lst_size//2 :]
        return sort(merge_sort(lst_a), merge_sort(lst_b))

LISTA = [random.randint(0, 100) for _ in range(100000)]

s = time.perf_counter()
r = merge_sort(LISTA.copy())
e = time.perf_counter() - s
# print(r)
print(f"Merge: in {e}")

s = time.perf_counter()
r = quicksort(LISTA.copy())
e = time.perf_counter() - s
# print(r)
print(f"QuickSort: in {e}")