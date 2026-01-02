def examA():
    S = SI()
    T = "AKIHABARA"
    ans = "YES"
    d = defaultdict(int)
    L = len(T); cur = 0
    for s in S:
        d[s] +=1
        while(cur<L):
            if s==T[cur]:
                break
            cur +=1
        if cur>=L:
            ans = "NO"
            break
        cur += 1
    if d["K"]<1 or d["I"]<1 or d["H"]<1 or d["B"]<1 or d["R"]<1:
        ans = "NO"
    print(ans)
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
    examA()
