#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

# 解説AC
# クルスカルでどのように最小全域木を作るかというと
# 辺ソートして小さい順に辺を見る
# ↓
# その辺が非連結成分どおしをつなぐなら追加
#
# 今回の場合pi,qjを合わせてソートする
# ↓
# piなら(i+1,y)と(i,y)の要素が連結成分になったとして考えられる
# qjなら(x,j+1)と(x,j)の要素が連結成分になったとして考えられる
# ↑
# これがどういうことかというと今piを辺に追加するとして,追加したなら
# qjによって連結成分になった分のyをつながなくても良い((i+1,y)と(i,y)を
# 連結にする際にすでに(i,y)と(i,y+1)は連結になっているため(i+1,y)と(i,y)を
# 連結にしたら(i+1,y+1) と(i,y)も連結になる))
#
# (5×5)追加する辺は
# x=1, y=1, x=3, x=4, y=3, x=2, y=2, y=4 の順番
#
#         1                       2                        3        
# o   o   o   o   o       o - o   o   o   o        o - o   o   o   o
#                    x=1                     y=1                    
# o   o   o   o   o       o - o   o   o   o        o - o   o   o   o
#                    add                     add                    
# o   o   o   o   o  ==>  o - o   o   o   o  ===>  o - o   o   o   o
#                    plus                    plus                   
# o   o   o   o   o       o - o   o   o   o        o - o   o   o   o
#                    5edg                    4edg      |   |   |   | 
# o   o   o   o   o       o - o   o   o   o        o - o   o   o   o
#
# 
#         3                       4                        5        
# o - o   o   o   o       o - o   o - o   o        o - o   o - o - o
#                    x=3                     x=4                    
# o - o   o   o   o       o - o   o - o   o        o - o   o - o - o
#                    add                     add                    
# o - o   o   o   o  ==>  o - o   o - o   o  ===>  o - o   o - o - o
#                    plus                    plus                   
# o - o   o   o   o       o - o   o - o   o        o - o   o - o   o
#     |   |   |   |  4edg     |   |   |   |  4edg      |   |   |   |
# o - o   o   o   o       o - o   o   o   o        o - o   o   o - o
#
# (4, 5 で共通するようにy = 1か2のやつはどっちでもいい(これが連結になることによる辺を追加しなくて良くなるイメージ))
# 
#         5                       6                        7        
# o - o   o - o - o       o - o   o - o - o        o - o - o - o - o
#                    y=3                     x=2                    
# o - o   o - o - o       o - o   o - o - o        o - o - o - o - o
#                    add      |   |          add       |   |        
# o - o   o - o - o  ==>  o - o   o - o - o  ===>  o - o   o - o - o
#                    plus                    plus                   
# o - o   o - o   o       o - o   o - o   o        o - o - o - o   o
#     |   |   |   |  2edg     |   |   |   |  3edg      |   |   |   |
# o - o   o   o - o       o - o   o   o - o        o - o   o   o - o
#
#
#
#         7                       8                        9        
# o - o - o - o - o       o - o - o - o - o        o - o - o - o - o
#                    y=2                     y=4       |            
# o - o - o - o - o       o - o - o - o - o        o - o - o - o - o
#     |   |          add      |   |          add       |   |        
# o - o   o - o - o  ==>  o - o   o - o - o  ===>  o - o   o - o - o
#                    plus         |          plus          |        
# o - o - o - o   o       o - o - o - o   o        o - o - o - o   o
#     |   |   |   |  1edg     |   |   |   |  1edg      |   |   |   |
# o - o   o   o - o       o - o   o   o - o        o - o   o   o - o
#
# 後はこれを実装するだけ
#
# 二つを合わせてソートするという考えは良かったけどサンプルケースに特化しすぎた。。
# もう少し考察でたどり着きたかった
#  
# solve
def solve():
    w, h = LI()
    a = []
    x, y = 0, 1
    for _ in range(w):
        a.append((II(), x))
    for _ in range(h):
        a.append((II(), y))
    a.sort()
    plus_x = h + 1
    plus_y = w + 1
    ans = 0
    for ai, xy in a:
        if xy:
            ans += ai * plus_y
            plus_x -= 1
        else:
            ans += ai * plus_x
            plus_y -= 1
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
