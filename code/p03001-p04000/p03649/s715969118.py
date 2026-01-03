import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n = int(input())
    aa = LI()
    change = True
    ps = 0
    ans = 0
    cnt = [0] * n
    while change:
        change = False
        sumk = 0
        for i in range(n):
            aa[i] += ps
            a = aa[i]
            if a <= n - 1: continue
            change = True
            k = a // n
            aa[i] -= (n + 1) * k
            cnt[i] += k
            sumk += k
            ans += k
        # print(ps,sumk,ans,aa)
        ps = sumk
    print(ans)

main()
