import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n,m = LI()
    r = 0
    d = collections.defaultdict(set)
    for _ in range(m):
        a,b = LI()
        d[a].add(b)
        d[b].add(a)
    for a in itertools.permutations(range(2,n+1)):
        if a[0] not in d[1]:
            continue
        f = True
        for i in range(len(a)-1):
            if a[i] not in d[a[i+1]]:
                f = False
                break
        if f:
            r += 1

    return r


print(main())
