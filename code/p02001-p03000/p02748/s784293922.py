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
    a,b,m=MI()
    aa=LI()
    bb=LI()
    ans=min(aa)+min(bb)
    for _ in range(m):
        x,y,c=MI()
        x,y=x-1,y-1
        ans=min(ans,aa[x]+bb[y]-c)
    print(ans)

main()