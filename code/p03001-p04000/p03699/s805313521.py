import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n = ni()
s = [ni() for _ in range(n)]

sm = sum(s)

s.sort()
not10min = sm

for si in s:
    if si%10 != 0:
        not10min = si
        break

if sm%10 == 0:
    print(sm - not10min)
else:
    print(sm)