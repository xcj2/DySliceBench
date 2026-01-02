import sys
from collections import Counter

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def nCr(com_n, com_r):
        return fac[com_n] * inv[com_r] * inv[com_n - com_r] % md

    n, k = MI()
    aa = LI()

    md = 10 ** 9 + 7
    n_max = n
    fac = [1] * (n_max + 1)
    inv = [1] * (n_max + 1)
    for i in range(2, n_max + 1): fac[i] = fac[i - 1] * i % md
    inv[n_max] = pow(fac[n_max], md - 2, md)
    for i in range(n_max - 1, 1, -1): inv[i] = inv[i + 1] * (i + 1) % md

    cnt = Counter(aa)
    allp = nCr(n, k)
    pa = 10 ** 10
    ans = 0
    l = 0
    for a, c in sorted(cnt.items()):
        if pa == 10 ** 10:
            pa = a
            l += c
            continue
        d = a - pa
        if l >= k and n - l >= k:
            ans += d * (allp - nCr(l, k) - nCr(n - l, k))
        elif l >= k:
            ans += d * (allp - nCr(l, k))
        elif n - l >= k:
            ans += d * (allp - nCr(n - l, k))
        else:
            ans += d * allp
        ans %= md
        l += c
        pa = a
    print(ans)

main()
