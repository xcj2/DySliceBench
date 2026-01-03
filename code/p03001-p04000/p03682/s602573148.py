import sys
read = sys.stdin.read
from operator import itemgetter
from copy import deepcopy
from collections import deque
def main():
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
            par[x] += par[y]
            par[y] = x
            return True
    def same(x, y):
        return find(x) == find(y)
    def size(x):
        return -par[find(x)]
    def members(x):
        root = find(x)
        return [i for i in range(n) if find(i) == root]
    def roots():
        return [i for i, x in enumerate(par) if x < 0]

    # input
    n = int(input())
    m = map(int, read().split())
    # inputされたノード座標のリストをｘ座標とｙ座標それぞれでソート。
    mm = zip(m, m)
    cnt = 0
    nodes = []
    nodes_a = nodes.append
    for a, b in mm:
        # nodes_a(x座標、y座標、ノード名) ※ノード名は0origin。union-findを使うため。
        nodes_a((a, b, cnt))
        cnt += 1
    nodes.sort(key=itemgetter(0))
    nodes_y = deepcopy(nodes)
    nodes_y.sort(key=itemgetter(1))
    # ノード座標リストからｘ軸とｙ軸それぞれで「隣接するノードをむすぶ辺」のリストをedgesに格納。
    edges = []
    for i1 in range(n - 1):
        # 辺のコスト、端のノード２つ
        edges.append((nodes[i1+1][0] - nodes[i1][0], nodes[i1][2], nodes[i1+1][2]))
        edges.append((nodes_y[i1+1][1] - nodes_y[i1][1], nodes_y[i1][2], nodes_y[i1+1][2]))
    # 「コストが小さい順」でソート
    edges.sort(key=itemgetter(0))
    # union-findをつかってクラスカル法をする。
    par = [-1] * n  # union-find用のデータ初期化
    edges = deque(edges)  # edgesを左から１つずつpopするのでdequeに変換。
    r = 0  # rに「森に加えた辺のコスト」を加算していく
    while edges:
        e = edges.popleft()
        if not same(e[1], e[2]):
            r += e[0]
            unite(e[1], e[2])
    print(r)

if __name__ == '__main__':
    main()
