import sys
from collections import defaultdict
import heapq

class Dijkstra():
    def __init__(self):
        self.edges = defaultdict(list)
    
    def add_edge(self, a, b, cost, directed=False):
        self.edges[a].append((b,cost))
        if not directed:
            self.edges[b].append((a,cost))
        
    def delete_edge(self, a, b):
        self.edges[a] = [item for item in self.edges[a] if item[0] != b]
        self.edges[b] = [item for item in self.edges[a] if item[0] != a]

    def Dijkstra_search(self, start=0):
        '''
        Returns min distances to every node from start node(input).
        '''

        # defaultdict to store minimum cost to visit each node
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0 # start node is zero-cost

        # initialize a priorit queue with heapq
        q = []
        heapq.heappush(q, (0, start))

        # store flags for each node to mark if the node has been visited
        if_visited = defaultdict(bool)

        while q:
            # search from a new node whose cost is known to be minimum among items in queue 
            cost_current, node_current = heapq.heappop(q)
            
            # skip if the node has already been visited
            if if_visited[node_current]:
                continue
            
            else:
                if_visited[node_current] = True

                # visit adjacent nodes
                for node_visiting, cost_visiting in self.edges[node_current]:

                    if if_visited[node_visiting]: # check if already visited
                        continue
                    
                    cost_cumulative = cost_current + cost_visiting

                    if cost_cumulative < distances[node_visiting]: # check if current path is worthy updating
                        distances[node_visiting] = cost_cumulative
                        heapq.heappush(q, (cost_cumulative, node_visiting))

        return distances


input = sys.stdin.readline
N = int(input())
g = Dijkstra()

while True:
    s = input()
    if s == '':
        break
    
    a, b, c = map(int, s.rstrip().split())
    a -= 1
    b -= 1
    g.add_edge(a,b,c)

distance = g.Dijkstra_search()

for x in distance:
    if distance[x] % 2 == 0:
        print(0)
    else:
        print(1)