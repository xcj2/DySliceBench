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
p = list(li())

ans = 0
cnt = 1
while cnt <= n:
    if p[cnt-1] == cnt:
        if cnt < n:
            cnt += 2
        elif cnt == n:
            cnt += 1

        ans += 1

    else:
        cnt += 1

print(ans)