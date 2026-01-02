#
# 　　  ⋀_⋀　 
#　　  (･ω･)  
# .／ Ｕ ∽ Ｕ＼
#  │＊　合　＊│
#  │＊　格　＊│ 
#  │＊　祈　＊│ 
#  │＊　願　＊│ 
#  │＊　　　＊│ 
#      ￣
#
import sys
input=sys.stdin.readline
from math import floor,ceil,sqrt,factorial,log #log2ないｙｐ
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import copy
inf=float('inf')
mod = 10**9+7
def INT_(n): return int(n)-1
def MI(): return map(int,input().split())
def MF(): return map(float, input().split())
def MI_(): return map(INT_,input().split())
def LI(): return list(MI())
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return list(MF())
def LIN(n:int): return [I() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]
def LLIN_(n: int): return [LI_() for _ in range(n)]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def I(): return int(input())
def F(): return float(input())
def ST(): return input().replace('\n', '')
def main():

    N = I()
    XY = LLIN(N)
    dic = defaultdict(lambda :-1)
    for i, (x, y) in enumerate(XY):
        dic[(x, y)] = i
    
        

    # UnionFind
    class UnionFind():
        def __init__(self, n):
            self.nodes=[-1] * n  # nodes[x]: 負なら、絶対値が木の要素数

        def get_root(self, x):
            # nodes[x]が負ならxが根
            if self.nodes[x] < 0:
                return x
            # 根に直接つなぎ直しつつ、親を再帰的に探す
            else:
                self.nodes[x]=self.get_root(self.nodes[x])
                return self.nodes[x]

        def unite(self, x, y):
            root_x=self.get_root(x)
            root_y=self.get_root(y)
            # 根が同じなら変わらない
            # if root_x == root_y:
            # pass
            if root_x != root_y:
                # 大きい木の方につないだほうが計算量が減る
                if self.nodes[root_x] < self.nodes[root_y]:
                    big_root=root_x
                    small_root=root_y
                else:
                    small_root=root_x
                    big_root=root_y
                self.nodes[big_root] += self.nodes[small_root]
                self.nodes[small_root]=big_root

    if N == 1:
        print(1)
        exit()
    ans = inf
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            p = XY[i][0] - XY[j][0]
            q = XY[i][1] - XY[j][1]
            uf = UnionFind(N)
            mini_ans = 0
            for (x, y) in XY:
                if dic[(x - p, y - q)] != -1:
                    uf.unite(dic[(x, y)], dic[(x - p, y - q)])
                if dic[(x + p, y + q)] != -1:
                    uf.unite(dic[(x, y)], dic[(x + p, y + q)])
            for i in range(N):
                if uf.nodes[i] < 0:
                    mini_ans += 1
            ans = min(mini_ans, ans)
    print(ans)
    """pre_exist = set()
    pre_exist.add((XY[i][0], XY[i][1]))
    mini_ans = 1
    for (x, y) in XY:
        found = False
        for (px, py) in pre_exist.copy():
            #print(pre_exist,x,y,px,py,mini_ans,"#",p,q)
            if (x, y) == (px, py):
                found = True
                continue
            dx = px - x
            dy = py - y
            if (dx-p==0 and dy-q==0) or (dx+p==0 and dy+q==0):
                found = True
                break
        pre_exist.add((x,y))
        if not found:
            mini_ans += 1"""
                        
if __name__ == '__main__':
    main()