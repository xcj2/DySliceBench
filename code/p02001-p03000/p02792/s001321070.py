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
    cnt=[[0]*10 for _ in range(10)]
    for x in range(1,n+1):
        l=int(str(x)[0])
        r=x%10
        cnt[l][r]+=1
    ans=0
    for l in range(1,10):
        for r in range(1,10):
            ans+=cnt[l][r]*cnt[r][l]
    print(ans)

main()