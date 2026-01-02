import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, H = LI()
    ab = []
    for i, _ in enumerate(range(N)):
        _ab = LI()
        ab.append((_ab[0], _ab[1], i))
    a_max, b_max, a_max_i = sorted(ab, key=lambda x:x[0])[-1]
    ab = sorted(ab, key=lambda x:x[1])[::-1]
    cnt = 0
    i = 0

    while i < N and H > 0:
        a, b, ken_i = ab[i]
        if b < a_max:
            break
        H -= b
        cnt += 1
        i += 1

    if H > 0:
        cnt += (math.ceil(H / a_max))

    print(cnt)
    
main()

