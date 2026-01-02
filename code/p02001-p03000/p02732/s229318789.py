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
    n = II()
    A = LI()

    memo = {}
    for a in A:
        memo[a] = memo.get(a, 0) + 1

    def choose2(a):
        if a == 0: return 0
        return a * (a-1) // 2

    # print(memo)
    ans = 0
    for k, v in memo.items():
        ans = ans + choose2(v)
    # print(ans)

    for a in A:
        print(ans - choose2(memo[a]) + choose2(memo[a] - 1))


if __name__ == '__main__':
    solve()
