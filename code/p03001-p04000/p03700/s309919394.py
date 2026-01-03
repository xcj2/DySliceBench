import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def ok(m):
        an=m
        for h in hh:
            d=h-b*m
            if d>0:
                an-=(d+a-b-1)//(a-b)
            if an<0:return False
        return True

    n,a,b=MI()
    hh=[int(input()) for _ in range(n)]
    mx=max(hh)
    l=mx//a-1
    r=mx//b+2
    while l+1<r:
        m=(l+r)//2
        if ok(m):r=m
        else:l=m
    print(r)

main()