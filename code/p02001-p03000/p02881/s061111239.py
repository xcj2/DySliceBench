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

    i = 1
    ans = 1001001001001
    while i*i <= n:
        if n % i == 0:
            j = n // i
            step = i + j - 2
            # print(i, j, step)
            ans = min(step, ans)
        i += 1

    print(ans)


if __name__ == '__main__':
    solve()
