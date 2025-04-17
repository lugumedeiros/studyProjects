"""Code that I used to learn about some algorithms"""

from collections import deque
import random
import time
import heapq

class Sort:
    @staticmethod
    def insertsort(lst):
        """O(n) Ω(n^2) avr(n^2), Space Θ(1), No recursion"""
        for i in range(len(lst)):
            for j in range(i):
                pointer = (i - j)
                left = lst[pointer - 1]
                right = lst[pointer]
                if left > right:
                    lst[pointer] = left
                    lst[pointer - 1] = right
                else:
                    break
        
        return lst

    def quicksort(lst):
        """O(nlogn) Ω(n^2) avr(nlogn), Space Θ(n), Has recursion"""
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]
            less = [x for x in lst if x < pivot]
            equal = [x for x in lst if x == pivot]
            more = [x for x in lst if x > pivot]
            return Sort.quicksort(less) + equal + Sort.quicksort(more)

    def merge_sort(lst):
        """Θ(nlogn), Space Θ(n), Has recursion"""
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
            return sort(Sort.merge_sort(lst_a), Sort.merge_sort(lst_b))
        
    def heap_sort(array):
        """Θ(nlogn), Space Θ(1), Has recursion"""
        heap = Heap.Min_heap(array)
        heap.heapsort()
        return heap.heap
    
class Search:
    @staticmethod
    def bfs_search_bad(graph, start_search, item_search):
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

    def bfs_search(graph, start_search, item_search):
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

    def dijkstra_bad2(graph, start):
        """I tried to make my own code for the dijkstra algorithm but it ended like a bfs search with distance mapping
        The main problem is that it will watse time because the order of searching is decided by the graph input,
        and not about the shortest path first, but in the end works and it has the complexity of a bfs lol.
        """

        # Create a FIFO and visited blacklist set
        fifo = deque([(start)])
        visited = set([])
        
        # Create distance map with invalid dist.
        distance = {node:float('inf') for node in graph}
        distance[start] = 0

        while len(fifo):
            node = fifo.popleft()
            visited.add(node)
            curr_dist = distance[node]
            for key, dist in graph[node]:
                dist += curr_dist
                # Test if current node was visited already
                if key in visited:
                    pass
                else:
                    fifo.append(key)
                    # Test if current declared distance is greater than new one
                    if distance[key] > dist:
                        distance[key] = dist
                    else:
                        pass
        return distance  

    def dijkstra_bad(graph, start):
        """ I never user heapq before, so this was my poor implementation of "correct" dijkstra, chapgpt is screaming tho...
        In the end this was potentially slower than my bfs version.
        """
        def get_smaller_value(map, blacklist):
            smll_v = float('inf')
            smll_k = None
            for key, value in map.items():
                if not (key in blacklist) and (value < smll_v):
                    smll_v = value
                    smll_k = key
            if smll_k == None:
                pass
            return smll_k

        set_visited = set([]) # List with all searched nodes
        map_dist = {node:float('inf') for node in graph} # List with the updated distances from start
        map_dist[start] = 0

        while len(set_visited) < len(map_dist):
            node = get_smaller_value(map_dist, set_visited)
            if node is None: break
            set_visited.add(node)
            current_dist = map_dist[node]

            for sub_node, sub_dist in graph[node]:
                sub_dist += current_dist
                if sub_node in set_visited:
                    pass
                else:
                    if sub_dist < map_dist[sub_node]:
                        map_dist[sub_node] = sub_dist

        return map_dist
                    
    def dijkstra(graph, start):
        """This is the correct python code for "dijksjktsra" i think... I used heapq this time, as adviced by chatgpt."""
        map_dist = {node:float('inf') for node in graph}
        map_dist[start] = 0
        to_visit = [(0, start)]

        while len(to_visit) > 0:
            current_dist, node = heapq.heappop(to_visit)

            for sub_node, sub_dist in graph[node]:
                sub_dist += current_dist

                if sub_dist < map_dist[sub_node]:
                    map_dist[sub_node] = sub_dist
                    heapq.heappush(to_visit, (sub_dist, sub_node))

        return map_dist

    def bin_search(lst, value):
        idx = len(lst) // 2
        midd = lst[idx]
        if midd == value:
            return idx
        elif len(lst) == 1:
            return None
        elif midd < value:
            return Search.bin_search(lst[idx:], value)
        else:
            return Search.bin_search(lst[:idx], value)

class Specific:
    @staticmethod
    def findCrossoverIndex(x, y, left=0, right=None):
        """Binary Search algorithm to find an index in two lists in which the first
        index has x>y and the second y>x"""
        right = len(x) if right is None else right
        mid = (right + left) // 2

        if mid == len(x):
            return None
        
        if x[mid] > y[mid]:
            if x[mid+1] < y[mid+1]:
                return mid
            else:
                return Specific.findCrossoverIndex(x, y, left=mid+1, right=right)
        else:
            return Specific.findCrossoverIndex(x, y, left=left, right=mid-1)
        
    def integerCubeRoot(n, left=0, right=None):
        """Binary search algorithm to find the integer cube root of positive value given"""
        if n <= 1:
            return n
        
        cube = lambda x: x*x*x
        right = n-1 if right is None else right
        mid = (left + right)//2
        
        if cube(mid) == n:
            return mid
        elif cube(mid) < n:
            if cube(mid+1) > n:
                return mid
            else:
                return Specific.integerCubeRoot(n, mid+1, right)
        else:
            return Specific.integerCubeRoot(n, left, mid-1)

class Heap:
    @staticmethod

    class Max_heap:
        def __init__(self, array):
            self.heap = array
            self.heapfy()

        def _swap(self, x, y, array):
            """Swap 2 idx from array"""
            assert x <= len(array) and y <= len(array)
            
            temp_x = array[x]
            array[x] = array[y]
            array[y] = temp_x
            return array

        def _get_children(self, idx, array):
            """get quantity of children if any at all"""
            array_max = len(array) - 1
            l_child_idx = ((idx + 1)* 2) - 1
            if l_child_idx > array_max:
                return False
            elif l_child_idx == array_max:
                return 1
            else:
                return 2
            
        def _bubble_down(self, idx, array):
            l_child = lambda x: ((x + 1) * 2) - 1

            has_child = self._get_children(idx, array)

            if not has_child:   # Has no children
                return array
            elif has_child == 1:    # Has only left child
                small_c = l_child(idx)
            else:   # Has 2 children
                left_c = l_child(idx)
                rigth_c = left_c + 1
                small_c = left_c if array[left_c] > array[rigth_c] else rigth_c
            
            if array[idx] < array[small_c]: # Test if smaller children must swap with parent
                array = self._swap(idx, small_c, array)
                return self._bubble_down(small_c, array)
            else:
                return array
            
        def _bubble_up(self,idx, array):
            if idx <= 0:
                return array
            
            parent = ((idx + 1) // 2) - 1
            
            if array[parent] < array[idx]:
                array = self._swap(parent, idx, array)
                return self._bubble_up(parent, array)
            else:
                return array

        def heapfy(self):
            heap_len = (len(self.heap) // 2) -1
            for i in range(heap_len, -1, -1):
                self.heap = self._bubble_down(i, self.heap)
        
        def heapsort(self):
            self.heapfy()
            total_len = len(self.heap)

            for i in range((total_len-1), -1, -1):
                self.heap = self._swap(0, i, self.heap)
                self.heap = self._bubble_down(0, self.heap[:i]) + self.heap[i:]

            for i in range(total_len // 2):
                compl = (total_len - i) - 1
                self.heap = self._swap(i, compl, self.heap)

        def insert(self, value):
            self.heap.append(value)
            pos = len(self.heap) - 1
            self.heap = self._bubble_up(pos, self.heap)
        
        def delete(self, idx):
            last_pos = len(self.heap) - 1
            self.heap = self._swap(idx, last_pos, self.heap)
            self.heap = self.heap[:last_pos]

            parent = ((idx + 1) // 2) - 1
            if idx == 0:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] < self.heap[idx]:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] > self.heap[idx]:
                return self._bubble_up(idx, self.heap)
            else: return
        
        def pop(self):
            value = self.heap[0]
            self.delete(0)
            return value

    class Min_heap:
        def __init__(self, array):
            self.heap = array
            self.heapfy()

        def _swap(self, x, y, array):
            """Swap 2 idx from array"""
            assert x <= len(array) and y <= len(array)
            
            temp_x = array[x]
            array[x] = array[y]
            array[y] = temp_x
            return array

        def _get_children(self, idx, array):
            """get quantity of children if any at all"""
            array_max = len(array) - 1
            l_child_idx = ((idx + 1)* 2) - 1
            if l_child_idx > array_max:
                return False
            elif l_child_idx == array_max:
                return 1
            else:
                return 2
            
        def _bubble_down(self, idx, array):
            l_child = lambda x: ((x + 1) * 2) - 1

            has_child = self._get_children(idx, array)

            if not has_child:   # Has no children
                return array
            elif has_child == 1:    # Has only left child
                small_c = l_child(idx)
            else:   # Has 2 children
                left_c = l_child(idx)
                rigth_c = left_c + 1
                small_c = left_c if array[left_c] < array[rigth_c] else rigth_c
            
            if array[idx] > array[small_c]: # Test if smaller children must swap with parent
                array = self._swap(idx, small_c, array)
                return self._bubble_down(small_c, array)
            else:
                return array
            
        def _bubble_up(self,idx, array):
            if idx <= 0:
                return array
            
            parent = ((idx + 1) // 2) - 1
            
            if array[parent] > array[idx]:
                array = self._swap(parent, idx, array)
                return self._bubble_up(parent, array)
            else:
                return array

        def heapfy(self):
            heap_len = (len(self.heap) // 2) -1
            for i in range(heap_len, -1, -1):
                self.heap = self._bubble_down(i, self.heap)
        
        def heapsort(self):
            self.heapfy()
            total_len = len(self.heap)

            for i in range((total_len-1), -1, -1):
                self.heap = self._swap(0, i, self.heap)
                self.heap = self._bubble_down(0, self.heap[:i]) + self.heap[i:]

            for i in range(total_len // 2):
                compl = (total_len - i) - 1
                self.heap = self._swap(i, compl, self.heap)

        def insert(self, value):
            self.heap.append(value)
            pos = len(self.heap) - 1
            self.heap = self._bubble_up(pos, self.heap)
        
        def delete(self, idx):
            last_pos = len(self.heap) - 1
            self.heap = self._swap(idx, last_pos, self.heap)
            self.heap = self.heap[:last_pos]

            parent = ((idx + 1) // 2) - 1
            if idx == 0:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] < self.heap[idx]:
                return self._bubble_down(idx, self.heap)
            elif self.heap[parent] > self.heap[idx]:
                return self._bubble_up(idx, self.heap)
            else: return
        
        def pop(self):
            value = self.heap[0]
            self.delete(0)
            return value

    class MedianHeap:
        def __init__(self, array):
            self.min_heap = Heap.Min_heap(array)
            self.max_heap = Heap.Max_heap([])
            self._ort_and_split()

        def _sort_and_split(self):
            unsorted_arr = self.max_heap.heap + self.min_heap.heap
            sorting_heap = Heap.Min_heap(unsorted_arr)
            sorting_heap.heapsort()
            sorted_arr = sorting_heap.heap

            half_arr = -(len(sorted_arr) // -2)
            self.max_heap.heap = sorted_arr[:half_arr]
            self.min_heap.heap = sorted_arr[half_arr:]
            self.max_heap.heapfy()

        def peek(self):
            return self.max_heap.heap[0]
        
        def insert(self, value):
            self.min_heap.insert(value)
            self._sort_and_split()


            

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

def get_full_graph_weight():
    d = {}
    d["YOU"] = [("ALICE", 1),("BOB", 10)]
    d["ALICE"] = [("ANUJ", 4), ("PEGGY", 2), ("BOB", 1)]
    d["BOB"] = [("TOM", 1), ("JON", 3)]
    d["ANUJ"] = []
    d["PEGGY"] = []
    d["TOM"] = []
    d["JON"] = [("CLAIR", 2), ("JAIR", 4)]
    d["CLAIR"] = [("JAIR", 1)]
    d["JAIR"] = []
    return d

def get_node_dist_graph():
    # Generate a large random graph with 1000 nodes
    num_nodes = 50
    graph_large = {f"N{i}": [] for i in range(num_nodes)}

    for i in range(num_nodes):
        num_edges = random.randint(2, 6)  # Each node connects to 2-6 other nodes
        neighbors = random.sample(range(num_nodes), num_edges)  # Random neighbors

        for neighbor in neighbors:
            if neighbor != i:  # No self-loops
                weight = random.randint(1, 100)  # Random weight (1-100)
                graph_large[f"N{i}"].append((f"N{neighbor}", weight))
    return graph_large

# GRAPH_W = get_node_dist_graph()
LISTA = [random.randint(0, 30) for _ in range(10)]

s = time.perf_counter()
r = Heap.MedianHeap(LISTA.copy())
e = time.perf_counter() - s
print(f"{r.peek()}\nResult: {e}\n")

print(r.max_heap.heap)
print(r.min_heap.heap)
