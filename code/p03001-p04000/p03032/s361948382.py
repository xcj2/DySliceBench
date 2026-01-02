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
    N, K = LI()
    V = LI()
    in_deq = deque()
    ans = 0
    for v in V:
        in_deq.append(v)
    for toru in range(K+1):
        for left_toru in range(toru+1):
            deq = copy.copy(in_deq)
            modosu = K - toru
            temochi = []
            right_toru = toru - left_toru
            # print('left_toru: {}, right_toru: {}, modosu: {}'.format(left_toru, right_toru, modosu))
            while len(deq) and left_toru > 0:
                x = deq.popleft()
                temochi.append(x)
                left_toru -= 1
            while len(deq) and right_toru > 0:
                x = deq.pop()
                temochi.append(x)
                right_toru -= 1
            temochi = sorted(temochi)[::-1]
            while len(temochi) > 0 and modosu > 0:
                extra = temochi[-1]
                if extra > 0:
                    break
                temochi = temochi[:-1]
                modosu -= 1
            ans = max(ans, sum(temochi))
    print(ans)
main()

