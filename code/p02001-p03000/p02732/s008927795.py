import sys
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
A = LMI()

d = defaultdict(int)
for a in A:
    d[a] += 1

# ad[i] := 数字iから作られるペアの数
ad = dict()
s = 0
for i, cnt in d.items():
    if cnt < 2:
        ad[i] = 0
    else:
        ad[i] = cnt * (cnt - 1) // 2
    s += ad[i]

for a in A:
    ans = s - ad[a]
    if d[a] >= 2:
        ans += (d[a] - 1) * (d[a] - 2) // 2
    print(ans)