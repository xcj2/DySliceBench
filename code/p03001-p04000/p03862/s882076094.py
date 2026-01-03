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
    n,x=MI()
    aa=LI()
    ans=0
    for i in range(n-1):
        cur=max(aa[i]+aa[i+1]-x,0)
        ans+=cur
        aa[i+1]-=min(cur,aa[i+1])
    print(ans)

main()