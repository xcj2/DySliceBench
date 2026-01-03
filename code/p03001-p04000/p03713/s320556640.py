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
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
from math import floor,ceil,sqrt,factorial,log #log2ないｙｐ
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
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
    H,W = MI()
    S = H*W
    ans = inf
    for h in range(H):
        if not (H-h)&1 or not W&1:
            piece = [h*W]
            piece.append(W*(H-h)/2)
            ans = min(ans, max(piece)-min(piece))
        else:
            if (H-h)&1:
                piece = [h*W]
                piece.append((H-h-1)*W/2)
                piece.append((H-h+1)*W/2)
                ans = min(ans, max(piece)-min(piece))
            if W&1:
                piece = [h*W]
                piece.append((W-1)*(H-h)/2)
                piece.append((W+1)*(H-h)/2)
                ans = min(ans, max(piece)-min(piece))
        

    for w in range(W):
        if not (W-w)&1 or not H&1:
            piece = [w*H]
            piece.append(H*(W-w)/2)
            ans = min(ans, max(piece)-min(piece))
        else:
            if (W-w)&1:
                piece = [h*W]
                piece.append((W-w-1)*H/2)
                piece.append((W-w+1)*H/2)
                ans = min(ans, max(piece)-min(piece))
            if H&1:
                piece = [h*W]
                piece.append((H-1)*(W-w)/2)
                piece.append((H+1)*(W-w)/2)
                ans = min(ans, max(piece)-min(piece))
    print(int(ans))
if __name__ == '__main__':
    main()
