import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n=int(input())
aa=LLI(n)

def main():
    ans=sum(sum(ar) for ar in aa)//2
    fin=set()
    for w in range(n):
        aaw=aa[w]
        for u in range(n):
            if u==w:continue
            aau=aa[u]
            for v in range(u):
                if v==w:continue
                d=aau[w]+aaw[v]
                if d<aau[v]:
                    print(-1)
                    exit()
                if d==aau[v] and (u,v) not in fin:
                    ans-=d
                    fin.add((u,v))
    print(ans)

main()
