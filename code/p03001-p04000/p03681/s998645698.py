import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    n, m = MI()
    fac = [1, 1]
    for i in range(2, n + 5):
        fac.append(fac[-1] * i % md)
    if abs(n - m) > 1:
        print(0)
        exit()
    if n < m: n, m = m, n
    if n == m:
        ans = 2 * fac[n] ** 2 % md
    else:
        ans = fac[n] * fac[m] % md
    print(ans)

main()
