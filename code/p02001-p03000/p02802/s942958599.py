import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n,m=MI()
    ac=[False]*n
    wa=[0]*n
    for _ in range(m):
        p,s=input().split()
        p=int(p)-1
        if s=="AC":
            ac[p]=True
        else:
            if not ac[p]:
                wa[p]+=1
    s=sum(wa[i] for i in range(n) if ac[i])
    print(sum(ac),s)

main()