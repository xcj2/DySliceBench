import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n=II()
    aa=[]
    cnt=[0]*200005
    for _ in range(n):
        c=II()
        if not aa or aa[-1]!=c:aa.append(c)
    #print(aa)
    md=10**9+7
    ans=1
    for a in aa:
        cnt[a]=(cnt[a]+ans)%md
        ans=cnt[a]
    print(ans)

main()