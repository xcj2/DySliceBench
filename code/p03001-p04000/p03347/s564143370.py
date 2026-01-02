def examC():
    N = I(); A = [I() for _ in range(N)]
    cur = -1; ans = -1
    for i in range(N):
        if A[i]>cur+1:
            ans = -1
            break
        elif A[i]==cur+1:
            cur +=1
            ans +=1
        else:
            ans += A[i]
            cur = A[i]
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
    examC()
