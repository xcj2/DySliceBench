import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


k, x = LI()
ans = []
stone = k - 1
if x - stone >= -(10 ** 6):
    ans += list(range(x - stone, x))
else:
    ans += abs(-(10 ** 6) - x)

ans += [x]

if x - stone <= (10 ** 6):
    ans += list(range(x + 1,  x + stone + 1))
else:
    ans += abs((10 ** 6) - x)
print(*ans)
