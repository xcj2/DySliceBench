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
    examB()
