def examA():
    S = SI()
    cur = 0; ans = 0
    for i,s in enumerate(S):
        if s=="W":
            ans += i-cur
            cur +=1
    print(ans)
    return

def examB():
    N = I()
    A = LI(); A.sort(reverse = True)
    ans = 0
    c = Counter(A)
    for a in A:
        cur = (1 << a.bit_length()) - a
        if c[a]>0 and c[cur]>0:
            if a==cur:
                ans += c[a]//2
                c[a]=0
                continue
            n = min(c[a],c[cur])
            c[a] -= n; c[cur] -= n
            ans += n
#            print(a,cur,c)
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
    examB()
