import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n,m = li()
py = []
for _ in range(m):
    py.append(list(li()))

order = [{} for _ in range(n+1)]
cnt = [0]*(n+1)

for p,y in sorted(py, key=lambda x:x[1]):
    order[p].update({y: cnt[p]})
    cnt[p] += 1


for p,y in py:
    cnt[p] += 1
    ans = str(p).zfill(6) + str(order[p][y]+1).zfill(6)
    print(ans)