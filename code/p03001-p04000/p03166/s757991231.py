from collections import deque

class Graph:
    def __init__(self,size):
        self.graph = [ {
            'idx' : i,
            'to': [],
            'inputs' : 0,
        } for i in range(size) ]

    def add_node(self,start,end):
        self.graph[start]['to'].append(end)
        self.graph[end]['inputs'] += 1

    def topological_sort(self):
        inputs = [i['inputs'] for i in self.graph]
        no_inputs = deque([ i['idx'] for i in self.graph if i['inputs'] == 0])
        ans = []
        while no_inputs:
            vertex1 = no_inputs.popleft()
            ans.append(vertex1)
            for vertex2 in self.graph[vertex1]['to']:
                inputs[vertex2] -= 1
                if inputs[vertex2] == 0:
                    no_inputs.append(vertex2)
        return ans

def main():
    n,m = map(int, input().split())
    G = Graph(n)
    for _ in range(m):
        x,y = map(int, input().split())
        G.add_node(x-1,y-1)
    tp = G.topological_sort()
    dist = [0] * n
    for v in tp[::-1]:
        for t in G.graph[v]['to']:
            if dist[v] <= dist[t]:
                dist[v] = dist[t] + 1
    print(max(dist))

if __name__ == '__main__':
    main()