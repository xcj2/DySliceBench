import heapq
import sys

input = sys.stdin.readline
INF = 100100100

class Info:
    def __init__(self, argNodeId, argSumCost):
        self.nodeId = argNodeId
        self.sumCost = argSumCost
    def __lt__(self, arg):
        return self.sumCost < arg.sumCost


class Edge:
    def __init__(self, argTo, argCost):
        self.to = argTo
        self.cost = argCost


def main():
    n = int(input())
    minDist = [INF] * n
    graph = [[] for _ in range(n)]
    for _ in range (n):
        u, k, *cv = map(int, input().split())
        for i in range(k):
            graph[u].append(Edge(cv[2 * i], cv[2*i + 1]))
    minDist[0] = 0
    Q = []
    heapq.heappush(Q, Info(0, 0))
    while len(Q) > 0:
        u = heapq.heappop(Q)
        if u.sumCost > minDist[u.nodeId]:
            continue
        for edge in graph[u.nodeId]:
            if minDist[edge.to] > u.sumCost + edge.cost:
                minDist[edge.to] = u.sumCost + edge.cost
                heapq.heappush(Q, Info(edge.to, minDist[edge.to]))
    for i in range(n):
        print('{} {}'.format(i, minDist[i]))


if __name__ == '__main__': main()
