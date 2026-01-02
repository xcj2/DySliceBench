import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

s = lc()
n = len(s)

tol = [0]*n
tor = [0]*n
ans = [0]*n

# Rにいる子のLまでの距離
dist = 0
for i in range(n-1, -1, -1):
    if s[i] == "L":
        dist = 0
    else:
        dist += 1
        tol[i] = dist

# Lにいる子のRまでの距離
dist = 0
for i in range(n):
    if s[i] == "R":
        dist = 0
    else:
        dist += 1
        tor[i] = dist

# それぞれの最終的な位置
for j, tolj in enumerate(tol):
    if tolj == 0:
        continue
    elif tolj % 2:
        ans[j + tolj - 1] += 1
    else:
        ans[j + tolj] += 1

for j, torj in enumerate(tor):
    if torj == 0:
        continue
    elif torj % 2:
        ans[j - torj + 1] += 1
    else:
        ans[j -torj] += 1

print(*ans)


