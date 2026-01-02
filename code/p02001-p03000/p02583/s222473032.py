import sys
sys.setrecursionlimit(300000)
from itertools import combinations

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
L = LMI()

ans = 0
for a, b, c in combinations(L, 3):
    if a == b or b == c or c == a:
        continue
    if a + b > c and b + c > a and c + a > b:
        ans += 1
print(ans)
