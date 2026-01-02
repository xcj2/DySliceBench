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
s = [lc() for _ in range(n)]

ans = 0

stb_eda = 0
stb = 0
eda = 0

for si in s:
    stmp = "".join(si)
    ans += stmp.count("AB")
    if si[0] == "B" and si[-1] == "A":
        stb_eda += 1
    elif si[0] == "B":
        stb += 1
    elif si[-1] == "A":
        eda += 1

if stb >= eda:
    diff = min(stb - eda, stb_eda)
    eda += diff
    stb_eda -= diff

else:
    diff = min(eda - stb, stb_eda)
    stb += diff
    stb_eda -= diff


if eda > 0 or stb > 0:
    ans += min(eda, stb) + stb_eda
else:
    ans += min(eda, stb) + max(0, stb_eda-1)

print(ans)