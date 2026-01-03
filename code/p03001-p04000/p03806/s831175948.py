import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n,m1,m2 = LI()
    r = [[inf]*401 for _ in range(401)]
    r[0][0] = 0
    for a,b,c in [LI() for _ in range(n)]:
        for i in range(400-a,-1,-1):
            for j in range(400-b,-1,-1):
                if r[i][j] == inf:
                    continue
                if r[i+a][j+b] > r[i][j] + c:
                    r[i+a][j+b] = r[i][j] + c

    t = inf
    for k in range(1,401):
        k1,k2 = m1*k,m2*k
        if k1 > 400 or k2 > 400:
            break
        if r[k1][k2] < t:
            t = r[k1][k2]

    if t == inf:
        return -1
    return t


print(main())
