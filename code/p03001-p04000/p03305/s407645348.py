import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

def main():
    import collections
    import heapq

    class Dijkstra:
        def __init__(self):
            self.e = collections.defaultdict(list)

        def add(self, u, v, d):  # 無向グラフの場合
            self.e[u].append([v, d])
            self.e[v].append([u, d])

        def delete(self, u, v):
            self.e[u] = [_ for _ in self.e[u] if _[0] != v]
            self.e[v] = [_ for _ in self.e[v] if _[0] != u]

        def search(self, s):  # d[i]はsからiまでの最短距離
            d = collections.defaultdict(lambda: float('inf'))
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for uv, ud in self.e[u]:
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

    n, m, s, t = MI()

    G1 = Dijkstra()  #円だけ
    G2 = Dijkstra()  #スヌースだけ

    for i in range(m):
        u,v,a,b = MI()
        G1.add(u,v,a)
        G2.add(u,v,b)

    D1 = G1.search(s)
    D2 = G2.search(t)

    A = []

    for i in range(1, n + 1):
        A.append((D1[i] + D2[i], i))

    A.sort()

    b = 0
    for i in range(n):
        if i == 0:
            print(10 ** 15 - A[i][0])
        elif i < A[b][1]:
            print(10 ** 15 - A[b][0])
        else:
            while i >= A[b][1]:
                b += 1
            print(10 ** 15 - A[b][0])

if __name__ == '__main__':
    main()
