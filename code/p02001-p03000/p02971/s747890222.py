# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

from collections import Counter

def solve():
    n = II()
    A = [II() for _ in range(n)]
    c = Counter(A)
    c = sorted(c.items())[::-1]
    mx = c[0][0]
    mx_n = c[0][1]
    if mx_n == 1:
        mx2 = c[1][0]
        for a in A:
            if a == mx:
                print(mx2)
            else:
                print(mx)
    else:
        for _ in A:
            print(mx)


if __name__ == '__main__':
    solve()
