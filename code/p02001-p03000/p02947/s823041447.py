# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

from collections import Counter

def c2s(c):
    s = ''
    for key, val in c:
        # print(key, val)
        # s = f'{s}{key}{val}'
        s = '{}{}{}'.format(s, key, val)
    # print(s)
    return s

def choose2(n):
    if n == 1:
        return 0
    return n * (n - 1) // 2

def solve():
    n = II()
    S = ["".join(sorted(input())) for _ in range(n)]
    # print(S)

    jisho = {}
    for s in S:
        # c = sorted(Counter(s).items(), key=lambda x: x[0])
        # print(c)
        # key = c2s(c)
        jisho[s] = jisho.setdefault(s, 0) + 1
    # print(jisho)
    ans = 0
    for val in jisho.values():
        ans = ans + choose2(val)

    print(ans)

if __name__ == '__main__':
    solve()
