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
    n = II()
    aa = LI()
    # +から始めるパターン
    cs = 0
    ans1 = 0
    for i, a in enumerate(aa):
        cs += a
        if i % 2:
            if cs >= 0:
                ans1 += abs(-1 - cs)
                cs = -1
        else:
            if cs <= 0:
                ans1 += abs(1 - cs)
                cs = 1
    # -から始めるパターン
    cs = 0
    ans2 = 0
    for i, a in enumerate(aa):
        cs += a
        if i % 2:
            if cs <= 0:
                ans2 += abs(1 - cs)
                cs = 1
        else:
            if cs >= 0:
                ans2 += abs(-1 - cs)
                cs = -1
    print(min(ans1,ans2))

main()
