def examA():
    N = LI()
    N.sort()
    if N==[1,4,7,9]:
        print("YES")
    else:
        print("NO")
    return

def examB():
    S = SI()
    K = "keyence"
    for i in range(7):
        if S[:i]+S[-7+i:]==K:
            print("YES")
            return
    if S[:7]==K:
        print("YES")
        return
    print("NO")
    return

def examC():
    N = I()
    A = LI()
    B = LI()
    if sum(A)<sum(B):
        print(-1)
        return
    dis = [A[i]-B[i] for i in range(N)]
    dis.sort()
#    print(dis)
    cur = 0
    ans = bisect.bisect_left(dis,0)
    need = -sum(dis[:bisect.bisect_left(dis,0)])
    for i in range(N):
        if need<=cur:
            break
        cur += dis[-i-1]
        ans += 1
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examC()

"""

"""