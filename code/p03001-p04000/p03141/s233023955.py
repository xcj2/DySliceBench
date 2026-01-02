def examC():
    N = I()
    A = [0]*N; B = [0]*N
    for i in range(N):
        A[i], B[i] = LI()
    taka = 0; aoki = 0
    value = [[i] for i in range(N)]
    for i in range(N):
        cur = A[i]+B[i]
        value[i].append(cur)
    value.sort(key=lambda x:x[1],reverse = True)
#    print(value)
    for i in range(N):
        if i%2==0:
#            print(A[value[i][0]])
            taka += A[value[i][0]]
        else:
#            print(B[value[i][0]])
            aoki += B[value[i][0]]
    ans = taka-aoki
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
    examC()
