def examD():
    N, K = LI()
    A = [0]*N; B = [0]*N
    for i in range(N):
        A[i],B[i] = LI()
    ans = 0; bi = 32
    for i in range(bi+1):
        if K&(1<<(bi-i))==0:
            if i!=bi:
                continue
        mask = 2**(bi-i)
        for j in range(i):
            if K&(1<<(bi-j))==0:
                mask += 2**(bi-j)
#        print(i,mask)
        now = 0
        for i in range(N):
            if A[i]&mask>0:
                continue
#            print(A[i],B[i])
            now +=B[i]
        ans = max(ans,now)

    mask = K^(2**bi -1)
    now = 0
    for i in range(N):
        if A[i] & mask > 0:
            continue
        #            print(A[i],B[i])
        now += B[i]
    ans = max(ans, now)
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
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()
