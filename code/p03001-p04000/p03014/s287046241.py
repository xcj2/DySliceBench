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
from math import floor,ceil,sqrt,factorial
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left,bisect_right
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
    H, W = MI()
    S = [["#"] * W ]+ ["#"+ST()+"#" for _ in range(H)]
    up = [[0] * (W+2) for _ in range(H+2)]
    left = [[0]*(W+2) for _ in range(H+2)]
    right = [[0]*(W+2) for _ in range(H+2)]
    down = [[0] * (W + 2) for _ in range(H + 2)]
    
    for h in range(1, H+1):
        for w in range(1, W + 1):
            if S[h][w] == "#":
                continue
            else:
                up[h][w] = up[h-1][w] + 1
                left[h][w] = left[h][w-1] + 1
    for h in range(1, H+1)[::-1]:
        for w in range(1, W+1)[::-1]:
            if S[h][w] == "#":
                continue
            else:
                down[h][w] = down[h+1][w] + 1
                right[h][w] = right[h][w + 1] + 1
                
    ans = 0
    for h in range(1, H+1):
        for w in range(1, W + 1):
            if S[h][w] == ".":
                ans = max(ans, (left[h][w-1] + right[h][w+1]) + (up[h-1][w] + down[h+1][w])+1)
                #print(ans,h,w , left[h][w] , right[h][w]) , (up[h][w] , down[h][w])
                
    print(ans)

    """
    cumsum1 = [[] for _ in range(H)]
    cumsum2 = [[] for _ in range(W)]
    
    for h in range(H):
        for w in range(W):
            if w == 0:
                cumsum1[h].append(int(S[h][w] == "#"))
            else:
                cumsum1[h].append(cumsum1[h][-1] + (S[h][w] == "#"))
            if h == 0:
                cumsum2[w].append(int(S[h][w] == "#"))
            else:
                cumsum2[w].append(cumsum2[w][-1] + (S[h][w] == "#"))
    #print(*cumsum2,sep="\n") 
    left_right = [[0] * W for _ in range(H)]
    up_down = [[0] * H for _ in range(W)]
    sharp = False:
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                sharp = True

            else:

    ans=0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            else:
                c1 = cumsum1[h][w]
                c2 = cumsum2[w][h]
                #print((h, w), cumsum1[h], cumsum2[w], sep="\n")
                b1,b2,b3,b4 = bisect_right(cumsum1[h], c1) ,bisect_left(cumsum1[h], c1) , bisect_right(cumsum2[w], c2) , bisect_left(cumsum2[w], c2)
                num = b1 - b2 + b3 - b4 -3 +(b2==0) + (b4 == 0) 
                #num = bisect_right(cumsum1[h], c1) - bisect_left(cumsum1[h], c1) + bisect_right(cumsum2[w], c2) - bisect_left(cumsum2[w], c2)-1 + (h==0)+(w==0)
                #print(num,b1,b2,b3,b4)
                ans=max(ans,num)
    print(ans)"""
if __name__ == '__main__':
    main()