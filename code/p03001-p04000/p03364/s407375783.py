def examA():
    N = I()
    A = LI()
    d = defaultdict(int)
    d[0] = 1; cur = 0
    for i in A:
        cur +=i
        d[cur] +=1
#    print(d)
    ans = 0
    for i in d.values():
        ans +=i*(i-1)//2
    print(ans)
    return

def examB():
    N = I()
    S = [SI() for _ in range(N)]
    cur = 0
    for k in range(N):
        flag = True
        for i in range(N):
            for j in range(i+1,N):
                if S[i][j-k]!=S[j][i-k]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            cur +=1
    ans = cur*N
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
