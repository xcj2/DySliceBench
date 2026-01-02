def examB():
    N = I()
    bit = 0; yen = 0
    for _ in range(N):
        x, u = LSI()
        if u=="JPY":
            yen +=float(x)
        else:
            bit +=float(x)
    ans = bit*380000 + yen
    print(ans)


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
    examB()
