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
lst = []
for i in range(n):
    lst.append((i, a[i]))

lst.sort(key=lambda x: x[1])

ans = []
for i, _ in lst:
    ans.append(i+1)

print(*ans)