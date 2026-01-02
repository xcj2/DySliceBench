import bisect
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def main():
    n = I()
    a = LI()
    b = LI()
    c = LI()
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for bi in b:
        num_a = bisect.bisect_left(a, bi)
        num_c = n - bisect.bisect_right(c, bi)
        ans += num_a * num_c
    print(ans)


main()
