import sys
import heapq
input = sys.stdin.readline

class Edge:
    def __init__(self, id, node1=-1, node2=-1, cost=-1):
        self.id = id
        self.node1 = node1
        self.node2 = node2
        self.cost = cost
    
    def next(self, num):
        if num == self.node1:
            return self.node2
        elif num == self.node2:
            return self.node1
        else:
            return False

def main():
    N, M = map(int, input().split())

    edges = [list() for i in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edge = Edge(i, a, b, c)
        edges[a].append(edge)
        edges[b].append(edge)

    ans = set([i for i in range(M)])
    for start in range(N):
        q = []
        check = [False] * N
        costs = [-1] * N
        heapq.heappush(q, (0, start, None))
        used_edge = set()
        while len(q) > 0:
            cost, node, pre_edge = heapq.heappop(q)
            if check[node]:
                if costs[node] == cost:
                    used_edge.add(pre_edge)
                continue
            costs[node] = cost
            check[node] = True
            if pre_edge != None:
                used_edge.add(pre_edge)
            for edge in edges[node]:
                next_node = edge.next(node)
                if not check[next_node]:
                    heapq.heappush(q, (cost + edge.cost, next_node, edge.id))
        ans -= used_edge
    print(len(ans))




if __name__ == "__main__":
    main()