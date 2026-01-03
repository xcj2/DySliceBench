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

odd = 0
ml2 = 0
ml4 = 0

for ai in a:
    if ai % 2:
        odd += 1
    elif ai % 4:
        ml2 = 1
    else:
        ml4 += 1

print("Yes" if (odd + ml2) <= (ml4 + 1) else "No")