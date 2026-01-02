import heapq

INF = 10 ** 7

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W = ZZ()
    C = [ZZ() for _ in range(10)]
    A = [ZZ() for _ in range(H)]

    def dijkstra(s):
        que = list()
        heapq.heapify(que)
        cost = [INF] * (10)
        cost[s] = 0
        heapq.heappush(que, [cost[s], s])

        while que:
            v = heapq.heappop(que)
            if cost[v[1]] < v[0]: continue
            for i in range(10):
                if cost[i] > cost[v[1]] + C[v[1]][i]:
                    cost[i] = cost[v[1]] + C[v[1]][i]
                    heapq.heappush(que, [cost[i], i])
        return cost[1]

    mc = [INF] * 10
    for i in range(10): mc[i] = dijkstra(i)
    output = 0
    for i in range(H):
         for j in range(W):
             if A[i][j] == -1: continue
             output += mc[A[i][j]]
    print(output)

    return

if __name__ == '__main__':
    main()
