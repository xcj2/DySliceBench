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
s = [ns() for _ in range(n)]

ans = 0

x = y = z = 0

for si in s:
    # 内部のABカウント
    ans += si.count('AB')

    # 右端A かつ 左端B ... Z
    if si[:1] == 'B' and si[-1:] == 'A':
        z += 1

    # 右端A ... X
    elif si[-1:] == 'A':
        x += 1

    # 左端B ... Y
    elif si[:1] == 'B':
        y += 1

if z <= x and z <= y:
    ans += 2*z
    ans += min(x,y) - z

else:
    ans += min(z, x)
    ans += min(z, y)

    if z >= x and z >= y:
        if x == 0 and y == 0:
            ans += z-1
        else:
            ans += z - max(x,y)

print(ans)