import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    inf=10**9
    n,m=MI()
    s=[LI() for _ in range(n)]
    c=[LI() for _ in range(m)]
    ans=[0]*n
    for si,(sx,sy) in enumerate(s):
        mn=inf
        mi=0
        for ci,(cx,cy) in enumerate(c):
            d=abs(cx-sx)+abs(cy-sy)
            if d<mn:
                mn=d
                mi=ci
        ans[si]=mi
    for a in ans:
        print(a+1)

main()