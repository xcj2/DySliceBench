# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n = II()
    H = LI()

    ans = 0
    cnt = 0
    for j in range(1, n):
        i = j - 1
        hi = H[i]
        hj = H[j]
        # print(hi, hj, hi>=hj)
        if hi >= hj:
            cnt = cnt + 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    solve()
