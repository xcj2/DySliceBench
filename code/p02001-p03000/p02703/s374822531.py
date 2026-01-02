from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product
import sys
import bisect
import string
import math
import time

def I(): return int(input())
def S(): return input()
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def LI(): return [int(i) for i in input().split()]
def LI_(): return [int(i)-1 for i in input().split()]
def StoI(): return [ord(i)-97 for i in input()]
def ItoS(nn): return chr(nn+97)
def input(): return sys.stdin.readline().rstrip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]

class NeighborList():
    def __init__(self):
        self.neighbor = {}


class Dijkstra(object):
    def dijkstra(self, adj, start, goal=None):
        '''
        ダイクストラアルゴリズムによる最短経路を求めるメソッド
        入力
        adj: adj[i][j]の値が頂点iから頂点jまでの距離(頂点iから頂点jに枝がない場合，値はfloat('inf'))となるような2次元リスト(正方行列)
        start: 始点のID
        goal: オプション引数．終点のID
        出力
        goalを引数に持つ場合，startからgoalまでの最短経路を格納したリストを返す
        持たない場合は，startから各頂点までの最短距離を格納したリストを返す
        '''
        dist = {} # 始点から各頂点までの最短距離を格納する
        prev = {} # 最短経路における，その頂点の前の頂点のIDを格納する

        dist[start] = 0
        prev[start] = 0
        q = []                  # プライオリティキュー．各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
        heappush(q, (0, start)) # 始点をpush

        while len(q) != 0:
            prov_cost, src = heappop(q) # pop

            # プライオリティキューに格納されている最短距離が，現在計算できている最短距離より大きければ，distの更新をする必要はない
            if dist[src] < prov_cost:
                continue

            # 他の頂点の探索
            for dest in adj[src].neighbor.keys():
                cost = adj[src].neighbor[dest]#src→destのチェック

                if dest in dist.keys():
                    if dist[dest] > dist[src] + cost:#先のコスト(仮決定) > 今のコスト+移動するのにかかるコスト
                        dist[dest] = dist[src] + cost # distの更新
                        heappush(q, (dist[dest], dest)) # キューに新たな仮の距離の情報をpush
                        prev[dest] = src                      # 前の頂点IDを記録
                else:#訪れたことが無ければ
                    dist[dest] = dist[src] + cost # distの更新
                    heappush(q, (dist[dest], dest)) # キューに新たな仮の距離の情報をpush
                    prev[dest] = src                      # 前の頂点IDを記録

        if goal is not None:
            return self.get_path(start,goal, prev)
        else:
            return dist

    def get_path(self, start, goal, prev):
        '''
        始点startから終点goalまでの最短経路を求める
        '''
        path = [goal]           # 最短経路
        dest = goal

        # 終点から最短経路を逆順に辿る
        while prev[dest] != start:
            path.append(prev[dest])
            dest = prev[dest]

        path.append(start)

        # 経路をreverseして出力
        return list(reversed(path))


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True

MX = 2500

def trans(e, s):
    return MX * e + s


def main():
    N, M, S = MI()
    U = [0] * M
    V = [0] * M
    A = [0] * M
    B = [0] * M
    C = [0] * N
    D = [0] * N
    edges = [[] for i in range(N)]
    # cost = [[] for i in range(N * MX)]
    adj = {i:NeighborList() for i in range(N * MX)}

    for i in range(M):
        U[i], V[i], A[i], B[i] = MI()
        U[i] -= 1
        V[i] -= 1
        edges[U[i]].append((V[i], i))
        edges[V[i]].append((U[i], i))

    for i in range(N):
        C[i], D[i] = MI()

    for i in range(N):
        for j in range(0, MX):
            to = min(j + C[i], MX-1)
            # cost[trans(i, j)][trans(i, to)] = D[i]
            adj[trans(i, j)].neighbor[trans(i, to)] = D[i]
            for pair in edges[i]:
                to = pair[0]
                idx = pair[1]
                if j - A[idx] >= 0:
                    # cost[trans(i, j)][trans(to, j - A[idx])] = B[idx]
                    adj[trans(i, j)].neighbor[trans(to, j - A[idx])] = B[idx]

    S = min(2499, S)
    # print('S', S)
    d = Dijkstra()
    ret = d.dijkstra(adj, trans(0, S))
    # ret = dijkstra(cost, trans(0, S))

    # print()
    # for i in range(1, N):
    #     print(i, *['IINF' if v == IINF else "{:0=4}".format(v) for v in cost[i]])

    for i in range(1, N):
        ans = IINF
        for j in range(MX):
            # if j <= 4:
            #     print(i, j, cost[i][j])
            ans = min(ans, ret[trans(i, j)])
        print(ans)


if __name__ == '__main__':
    main()
