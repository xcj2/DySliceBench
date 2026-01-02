import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from itertools import product

def main():
    N, M = LI()
    kss = []
    for _ in range(M):
        kss.append(LI_()[1:])
    pp = LI()
    ans = 0
    for sw in product(range(2), repeat=N):
        ok = True
        for ks, p in zip(kss, pp):
            check = 0
            for k in ks:
                if sw[k]:
                    check += 1
            if check % 2 != p:
                ok = False
                break
        if ok:
            ans += 1
    return ans

print(main())