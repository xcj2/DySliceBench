import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')

def solve():
    n, x, y = MI()

    ans = [0] * (n-1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # print(i, j)
            d = min(j - i, abs(i - x) + 1 + abs(y - j))
            ans[d-1] += 1
    # print(ans)
    for a in ans:
        print(a)


if __name__ == '__main__':
    solve()
