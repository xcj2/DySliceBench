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

def yakusu(n):
    yakusu = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            yakusu.append(i)
            if n // i != i:
                yakusu.append(n//i)
    return yakusu
     
baisu = [False] * (10**6 + 1)
def main():
    N = I()
    A = LI()

    ok = 0
    for a in set(A):
        if baisu[a]:
            continue
        if not baisu[a]:
            num = a + a
            while num < 10**6+1:
                baisu[num] = True
                num += a
    s = collections.Counter(A)
    for a in A:
        if not baisu[a]:
            if s[a] > 1:
                continue
            ok += 1
    print(ok)
main()

