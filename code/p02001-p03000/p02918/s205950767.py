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

n, k = li()
s = ns()

if len(set(list(s))) == 1:
    print(n-1)
else:
    init = 0
    bef = ""
    for si in s:
        if si == bef:
            init += 1
        bef = si
    print(min(n-1, init + 2*k))