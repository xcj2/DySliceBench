import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

md=10**6+3
n_max = md-1
fac = [1]
for i in range(1, n_max + 1): fac.append(fac[-1] * i % md)
ifac = [1] * (n_max + 1)
ifac[n_max] = pow(fac[n_max], md - 2, md)
for i in range(n_max - 1, 1, -1): ifac[i] = ifac[i + 1] * (i + 1) % md

def main():
    for _ in range(II()):
        x,d,n=MI()
        if x==0:ans=0
        elif d==0:ans=pow(x,n,md)
        else:
            invd=pow(d,md-2,md)
            x=x*invd%md
            if x+n-1>=md:ans=0
            else:
                ans=fac[x+n-1]*ifac[x-1]*pow(d,n,md)%md
        print(ans)

main()