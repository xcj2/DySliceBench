import sys
import math
from collections import defaultdict, deque
from copy import deepcopy
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    H, W, M = MI()
    Hlist = [[0, i] for i in range(H)]
    Wlist = [[0, i] for i in range(W)]
    Dlist = [set() for i in range(H)]
    H_max = -float('inf')
    W_max = -float('inf')
    
    for i in range(M):
        h, w = MI()
        Hlist[h-1][0]+=1
        Wlist[w-1][0]+=1
        Dlist[h-1] |= {w-1}
        H_max = max(H_max, Hlist[h-1][0])
        W_max = max(W_max, Wlist[w-1][0])
    Hlist = set([temp[1] for temp in Hlist if temp[0] == H_max])
    Wlist = set([temp[1] for temp in Wlist if temp[0] == W_max])
    ans = H_max+W_max-1

    for index1 in Hlist:
        for index2 in Wlist:
            if not index2 in Dlist[index1]:
                ans += 1
                break
        else:
            continue
        break
    print(ans)

if __name__ == "__main__":
    main()