def examC():
    N = I()
    for h in range(1,3501):
        for w in range(1,3501):
            cur = 4*h*w - N*(h+w)
            if cur>0 and (N*h*w)%cur==0:
                n = (N*h*w)//cur
                print(h,n,w)
                exit()
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC()
