import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    n = int(input())
    aa = LI()
    cnt = [[0] * 2 for _ in range(61)]
    for a in aa:
        for i in range(61):
            cnt[i][a & 1] += 1
            a >>= 1
    #print(cnt)
    base = 1
    ans = 0
    for c0, c1 in cnt:
        ans += base * c0 * c1
        ans %= md
        base = base * 2 % md
    print(ans)

main()
