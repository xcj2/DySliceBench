def examA():
    A, P = LI()
    ans = (A*3+P)//2
    print(ans)
    return

def examB():
    N = I()
    SP = [[]for _ in range(N)]
    for i in range(N):
        SP[i] = LSI()
        SP[i][1] = int(SP[i][1])
        SP[i].append(i)
#    print(SP)
    SP = sorted(SP,key = lambda x:x[1], reverse = True)
    SP = sorted(SP,key = lambda x:x[0])
#    print(SP)
    for v in SP:
        print(v[2]+1)
    return

def examC():
    N, M = LI()
    S = [LI() for _ in range(M)]
    P = LI()
    ans = 0
    loop = 2**N
    for i in range(loop):
        flag = True
        d = defaultdict(bool)
        for j in range(N):
            if i&(1<<j)==(1<<j):
                d[j+1] = True
        for l,j in enumerate(S):
            cur = 0
            for k in range(1,j[0]+1):
                if d[j[k]]:
                    cur +=1
            if cur%2!=P[l]:
#                print(cur,l,i)
                flag = False
                break
        if flag:
            ans +=1
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
    examC()
