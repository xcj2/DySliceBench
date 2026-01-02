import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    import heapq
    import itertools

    def dijkstra(s, n):
        hq = [(0, s)]
        heapq.heapify(hq)  # リストを優先度付きキューに変換
        cost = [float('inf')] * n  # 行ったことのないところはinf
        cost[s] = 0  # 開始地点は0
        while hq:
            c, v = heapq.heappop(hq)
            if c > cost[v]:  # コストが現在のコストよりも高ければスルー
                continue
            for d, u in e[v]:
                tmp = d + cost[v]
                if tmp < cost[u]:
                    cost[u] = tmp
                    heapq.heappush(hq, (tmp, u))
        return cost



    N, M, R = MI()
    r = LI()
    e = [[]for _ in range(N)]
    dis_list = [[]for _ in range(N)]
    for i in range(M):
        a, b, c = MI()
        a, b = a - 1, b - 1
        e[a].append((c, b))
        e[b].append((c, a))
    for r_ in r:
        dis_list[r_ - 1] = dijkstra(r_ - 1, N)

    Ans_list = []
    P = itertools.permutations(r)
    for p in P:
        dis = 0
        for i in range(R - 1):
            dis += dis_list[p[i] - 1][p[i + 1] - 1]
        Ans_list.append(dis)
    ans = min(Ans_list)
    print(ans)

if __name__ == "__main__":
    main()
