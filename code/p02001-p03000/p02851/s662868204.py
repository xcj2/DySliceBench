from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n,k=MI()
    aa=LI()
    cs=[0]*(n+1)
    s=0
    for i,a in enumerate(aa,1):
        cs[i]=(cs[i-1]+a-1)%k
    #print(cs)
    cnt=defaultdict(int)
    ans=0
    for i,c in enumerate(cs):
        if i-k>=0:cnt[cs[i-k]]-=1
        ans+=cnt[c]
        cnt[c]+=1
    print(ans)

main()