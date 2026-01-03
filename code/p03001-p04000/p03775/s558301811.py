import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    s = int(math.sqrt(n))+1
    t = n
    for i in range(s,0,-1):
        if n % i == 0:
            t = max(n//i,i)
            break
    ti = 0
    while t > 0:
        ti += 1
        t //= 10
    return ti



print(main())
