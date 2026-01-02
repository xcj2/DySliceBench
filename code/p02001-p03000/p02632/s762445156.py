import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def nCr(com_n, com_r):
    if com_n < com_r: return 0
    return fac[com_n] * ifac[com_r] % md * ifac[com_n - com_r] % md

# combinationの準備
# md>n_maxの条件
md = 10 ** 9 + 7
n_max = 2000005
fac = [1]
for i in range(1, n_max + 1): fac.append(fac[-1] * i % md)
ifac = [1] * (n_max + 1)
ifac[n_max] = pow(fac[n_max], md - 2, md)
for i in range(n_max - 1, 1, -1): ifac[i] = ifac[i + 1] * (i + 1) % md

def main():
    k=II()
    s=SI()
    r=len(s)
    ans=0
    for i in range(k+1):
        ans=ans*26+pow(25,i,md)*nCr(i+r-1,r-1)%md
        ans%=md
    print(ans)

main()