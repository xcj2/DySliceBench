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
    s=SI()
    n=len(s)
    ans=0
    nxt=0
    for i in range(n-1,-1,-1):
        now=int(s[i])+nxt
        if now>5 or (i>0 and now==5 and int(s[i-1])>4):
            nxt=1
            ans+=10-now
        else:
            ans += now
            nxt = 0
    ans+=nxt
    print(ans)

main()