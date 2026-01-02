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
     
'''
def main():
    N, M = LI()
    digits = [-1 for _ in range(N)]
    for _ in range(M):
        s, c = LI()
        if N > 1 and s == 1 and c == 0:
            print("-1")
            return
        if digits[s-1] == -1:
            digits[s-1] = c
        else:
            if digits[s-1] != c:
                print("-1")
                return 
    for i, d in enumerate(digits):
        if N == 1 and i == 0 and d == 0:
            print(0)
            return
        if i == 0 and d == 0:
            print("-1")
            return 
        if i > 0 and d == -1:
            digits[i] = 0
        if i == 0 and d == -1:
            digits[i] = 1

    print(''.join([str(x) for x in digits]))
'''
def main():
    N, M = LI()
    q = []
    for _ in range(M):
        s, c = LI()
        q.append((s, str(c)))
    for x in range(0, 1000):
        flag = True
        x = str(x)
        if len(x) < N:
            continue
        for (s, c) in q:
            s -= 1
            if c != x[s]:
                flag = False
            
        if flag:
            print(x)
            return
    print("-1")

main()

