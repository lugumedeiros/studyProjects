"""Code that I used to learn about some algorithms"""

from collections import deque
import random
import time
import heapq

class Sort:
    @staticmethod
    def instersort(lst):
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
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]
            less = [x for x in lst if x < pivot]
            equal = [x for x in lst if x == pivot]
            more = [x for x in lst if x > pivot]
            return Sort.quicksort(less) + equal + Sort.quicksort(more)

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
            return sort(self.merge_sort(lst_a), self.merge_sort(lst_b))
    
class Search:
    @staticmethod
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

    def dijkstra(graph, start):
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

    def dijkstra2(graph, start):
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
                    
    def dijkstra3(graph, start):
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

GRAPH_W = get_node_dist_graph()
LISTA = [random.randint(0, 100) for _ in range(10)]

n_list = Sort.quicksort(LISTA.copy())
s = time.perf_counter()
r = Search.bin_search(n_list, 3)
e = time.perf_counter() - s
print(f"BFS: in {e}s\nResult: {r}")