from collections import Counter
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
    n=II()
    mx=10**6
    aa=LI()
    ac=Counter(aa)
    #print(aa)

    ok=[True]*(mx+1)
    ans=0
    for a,c in sorted(ac.items()):
        if ok[a]:
            if c==1:ans+=1
            for b in range(a*2,mx+1,a):
                ok[b]=False
    print(ans)

main()