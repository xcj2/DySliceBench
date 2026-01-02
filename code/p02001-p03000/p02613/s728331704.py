import sys
sys.setrecursionlimit(300000)
from collections import Counter

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
S = [input() for _ in range(N)]

c = Counter(S)
for label in ['AC', 'WA', 'TLE', 'RE']:
    print(label, 'x', c[label])