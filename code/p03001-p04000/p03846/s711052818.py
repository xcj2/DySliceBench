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
    def ok(n,aa):
        if n&1:
            if aa[0]!=0:return False
            b=2
            first=True
            for a in aa[1:]:
                if a!=b:return False
                if first:first=False
                else:
                    b+=2
                    first=True
        else:
            b=1
            first=True
            for a in aa:
                if a!=b:return False
                if first:first=False
                else:
                    b+=2
                    first=True
        return True

    md=10**9+7
    n=II()
    aa=LI()
    aa.sort()
    if ok(n,aa):print(pow(2,n//2,md))
    else:print(0)

main()
