import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    n = II()
    cc = LI()
    cc.sort()
    exp2 = [1]
    for x in range(1, n + 1):
        exp2.append(exp2[-1] * 2 % md)
    #print(exp2)
    ans = 0
    for i, c in enumerate(cc):
        s = exp2[n - 1 - i]
        if n - i - 1 != 0: s += (n - 1 - i) * exp2[n - 2 - i]
        s *= exp2[i] * c
        ans = (ans + s) % md
    ans = ans * exp2[n] % md
    print(ans)

main()
