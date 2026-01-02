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

n = ni()
a = list(li())
MOD = 1000000007

next = [0,0,0]
ans = 1

for ai in a:
    cnt = next.count(ai)
    if cnt == 0:
        ans = 0
        break
    else:
        idx = next.index(ai)
        next[idx] += 1
        ans *= cnt
        ans %= MOD

print(ans)