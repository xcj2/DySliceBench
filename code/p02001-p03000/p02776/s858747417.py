# 解説動画の通り
# 前の提出間違ってた...ACしたけど
import sys
from bisect import *
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    def dfs(u):
        fin[u] = True
        for v, e in to[u]:
            if fin[v]: continue
            dfs(v)
            if xx[v]:
                ans.append(e + 1)
                xx[u] ^= 1

    n, m = MI()
    ab = [LI() for _ in range(n)]
    lr = [LI() for _ in range(m)]
    # (a,b)をaでソートして分ける
    # bは先頭と末尾に番兵の0を追加する（全部を0にするのが目標だから）
    aa = []
    bb = [0]
    for a, b in sorted(ab):
        aa.append(a)
        bb.append(b)
    bb.append(0)
    # print(aa)
    # print(bb)
    # bの差分列を作る
    xx = [b0 ^ b1 for b0, b1 in zip(bb, bb[1:])]
    # print(xx)
    # lrをxxのインデックスに対応させる
    lr = [(bisect_left(aa, l), bisect_right(aa, r)) for l, r in lr]
    # print(lr)
    # lrを辺、xxの要素を頂点としてグラフを作る
    to = defaultdict(list)
    for i, (l, r) in enumerate(lr):
        if l == r: continue
        to[l].append((r, i))
        to[r].append((l, i))
    # 各連結成分についてdfsする
    ans = []
    fin = [False] * (n + 1)
    for i in range(n + 1):
        if fin[i]: continue
        dfs(i)
        # 根が1のときは実現不可能なので-1を出力して終了
        if xx[i]:
            print(-1)
            exit()
    # 答えの出力
    ans.sort()
    print(len(ans))
    print(*ans)

main()
