import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7


import heapq
def prim_heap(n, edges):  # n: 最大の頂点番号+1, edges[頂点番号]=[[重み, 行き先],[重み, 行き先],...]. 無向グラフの場合は相方向有向グラフの表記にしておく。
    seen = [False] * n #True:不使用
    edgelist = []  # heapq
    for e in edges[0]:  # 頂点 0 から伸びる辺をすべて heapq に入れる。
        heapq.heappush(edgelist,e)
    seen[0] = True  # 頂点 0 は見たと記録する。
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)  # edgelist から最小の辺を1つ取り出す。
        if seen[minedge[1]]:  # その辺の行き先がすでに見た先だったら棄却して次へ。
            continue
        v = minedge[1]  # 行き先を v とする。
        seen[v] = True  # 頂点 v は見たと記録する。
        for e in edges[v]:  # 頂点 v から伸びる辺すべてについて、もしその行き先を見ていなかったら heapq に追加する。
            if not seen[e[1]]:
                heapq.heappush(edgelist,e)
        res += minedge[0]  # いま使った辺の重みを結果に加える。
    return res  # 最小全域木の全体の重みを出力する。



def main(): 
    N = II()
    pos_li = []
    for i in range(N):
        x,y = LI()
        pos_li.append((x,y,i))
    edges = [[] for _ in range(N)]
    # # すべての頂点を結ぶグラフを作ってその最小全域木を取ると、時間が足りない（二重ループが O(10^10)）。
    # for i in range(N):
    #     for j in range(N):
    #         weight = min(abs(pos_li[i][0] - pos_li[j][0]), abs(pos_li[i][1] - pos_li[j][1]))
    #         edges[i].append([weight, j])
    #         edges[j].append([weight, i])
    # # なので、座標でソートして、最も近い4点のみへ辺を伸ばす。
    pos_li.sort(key=lambda x: x[0])
    for k in range(N-1):
        x1, y1, p1 = pos_li[k]
        x2, y2, p2 = pos_li[k+1]
        weight = abs(x1-x2)
        edges[p1].append([weight, p2])
        edges[p2].append([weight, p1])

    pos_li.sort(key=lambda x: x[1])
    for k in range(N-1):
        x1, y1, p1 = pos_li[k]
        x2, y2, p2 = pos_li[k+1]
        weight = abs(y1-y2)
        edges[p1].append([weight, p2])
        edges[p2].append([weight, p1])

    # print(edges)
    print(prim_heap(N, edges))

main()