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
    n,k=MI()
    r,s,p=MI()
    t=S()
    ans=0
    ns=""
    for i in range(k):
        if t[i]=="r":
            ans+=p
            ns+="p"
        if t[i]=="p":
            ans+=s
            ns+="s"
        if t[i]=="s":
            ans+=r
            ns+="r"
    for i in range(k,n):
        if t[i]=="r" and ns[i-k]=="p":
            ns+="1"
            ans+=0
        if t[i]=="r" and ns[i-k]!="p":
            ns+="p"
            ans+=p
        if t[i]=="p" and ns[i-k]=="s":
            ns+="1"
            ans+=0
        if t[i]=="p" and ns[i-k]!="s":
            ns+="s"
            ans+=s
        if t[i]=="s" and ns[i-k]=="r":
            ns+="1"
            ans+=0
        if t[i]=="s" and ns[i-k]!="r":
            ns+="r"
            ans+=r
    print(ans)


if __name__ == "__main__":
    main()