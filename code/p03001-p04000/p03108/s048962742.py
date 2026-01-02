# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, m = LI()
    AB = [LI_() for _ in range(m)]
    AB.reverse()

    # マージテク
    par = [i for i in range(n)]  # 連結しているグループのリーダ
    node = [set([i]) for i in range(n)]  # グループに所属しているノードの集合

    def merge(x, y):
        # 既に連結済みなら何もしない
        if par[x] == par[y]:
            return 0
        x, y = par[x], par[y]
        size_x, size_y = len(node[x]), len(node[y])

        # 小さいグループを大きいグループにマージする. O(log(n))
        if size_x < size_y:
            x, y = y, x

        # ノードの移動とリーダの更新
        while node[y]:
            v = node[y].pop()
            par[v] = x
            node[x].add(v)

        # (xの連結数)*(yの連結数)だけ不満度が解消される
        return size_x * size_y

    res = [n * (n - 1) // 2]
    for a, b in AB:
        sub = merge(a, b)
        res.append(res[-1] - sub)

    res.pop()
    res.reverse()

    print(*res, sep='\n')


main()
