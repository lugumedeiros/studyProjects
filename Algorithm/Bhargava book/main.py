"""Code that I used to learn about some algorithms"""

from collections import deque
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
    
def bfs_search(graph, start_search, item_search):
    # Tried to do my own just from concepts, not so bad I think
    invalid_graph = []
    search_graph = graph[start_search]
    degree = 1
    
    while len(search_graph) > 0:
        if item_search in search_graph:
            print(f"item found!, {degree} items distant from start")
            break
        else:
            temp_graph = search_graph.copy()
            for key in search_graph:
                invalid_graph.append(key)
                temp_graph += graph[key]
            new_graph = []
            for key in temp_graph:
                if not key in invalid_graph:
                    new_graph.append(key)
        search_graph = new_graph
        degree += 1

def bfs_search2(graph, start_search, item_search):
    # This one I applied FIFO, first time I used this...
    degree = 0
    fifo = deque([(start_search, degree)]) # List of tuples
    invalid_keys = set([start_search])

    while len(fifo) > 0:
        key, degree = fifo[0]
        if key == item_search:
            print(f"item found!, {degree} items distant from start")
            return
        else:
            fifo.popleft()
            for subkey in graph[key]:
                if not subkey in invalid_keys:
                    fifo.append((subkey, degree + 1))


def get_full_graph():
    d = {}
    d["YOU"] = ["ALICE","BOB"]
    d["ALICE"] = ["ANUJ", "PEGGY"]
    d["BOB"] = ["TOM", "JON"]
    d["ANUJ"] = []
    d["PEGGY"] = []
    d["TOM"] = []
    d["JON"] = ["CLAIR", "JAIR"]
    d["CLAIR"] = []
    d["JAIR"] = []
    return d
GRAPH = get_full_graph()

LISTA = [random.randint(0, 100) for _ in range(100000)]

s = time.perf_counter()
r = bfs_search(GRAPH.copy(), "YOU", "JAIR")
e = time.perf_counter() - s
print(f"Sort(BFS): in {e}s")

s = time.perf_counter()
r = bfs_search2(GRAPH.copy(), "YOU", "JAIR")
e = time.perf_counter() - s
print(f"Sort(BFS): in {e}s")

# s = time.perf_counter()
# r = merge_sort(LISTA.copy())
# e = time.perf_counter() - s
# print(f"Merge: in {e}s")

# s = time.perf_counter()
# r = quicksort(LISTA.copy())
# e = time.perf_counter() - s
# print(f"QuickSort: in {e}s")