import sys
from random import choice,randint
inp=sys.stdin.readline
out=sys.stdout.write
flsh=sys.stdout.flush
 
sys.setrecursionlimit(10**9)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
 
def MI(): return map(int, inp().strip().split())
def LI(): return list(map(int, inp().strip().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines().strip()]
def LI_(): return [int(x)-1 for x in inp().strip().split()]
def LF(): return [float(x) for x in inp().strip().split()]
def LS(): return inp().strip().split()
def I(): return int(inp().strip())
def F(): return float(inp().strip())
def S(): return inp().strip()
def pf(s): return out(s+'\n')
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def main():
    n,a,b=MI()
    # n,a,b=randint(1,30),randint(1,10),randint(5,25)
    # print(n,a,b)
    if (b-a)%2==0:
        pf(str((b-a)//2))
    elif a==1 or b==n:
        pf(str((b-a+1)//2))
    else:
        mn = min(a-1,n-b)
        ans = (b-a+(mn*2)+1)//2
        ans = min([ans,n-a,b-1])
        pf(str(ans))

if __name__ == "__main__":
    main()