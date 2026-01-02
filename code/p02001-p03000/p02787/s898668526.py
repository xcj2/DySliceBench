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
    inf=10**9
    h,n=MI()
    aa=[]
    bb=[]
    for _ in range(n):
        a,b=MI()
        aa.append(a)
        bb.append(b)
    dp=[inf]*(h+1)
    dp[0]=0
    for i in range(h):
        pre=dp[i]
        for a,b in zip(aa,bb):
            ni=h if i+a>h else i+a
            if pre+b<dp[ni]:dp[ni]=pre+b
    print(dp[h])

main()