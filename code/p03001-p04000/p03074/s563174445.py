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


n,k = li()
s = ns()

cur = "1"
cum = [0]

for i, si in enumerate(s):
    if cur != si:
        cur = si
        cum.append(i)

cum.append(n)

if cur == "0":
    cum.append(n)


ans = 0
if k >= len(cum)//2:
    ans = n
else:
    for i in range(0, len(cum) - 2*k - 1, 2):
        ans = max(ans, cum[i + 2*k + 1] - cum[i])

print(ans)