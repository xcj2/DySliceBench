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

def get_yakusu(n):
    ans = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != 1:
                ans.add(i)
            if n // i != i:
                ans.add(n // i)
    return ans

def main():
    N = I()
    cnt = 0
    if N == 2:
        print(1)
        return
    yakusu = get_yakusu(N)
    n1yakusu = get_yakusu(N-1)
    for n in yakusu:
        cpN = N
        while True:
            if cpN % n == 0:
                cpN = cpN // n
            else:
                break
        if cpN % n == 1:
            cnt += 1
    cnt += len(n1yakusu)
    print(cnt)
main()

