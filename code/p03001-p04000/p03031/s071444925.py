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

n, m = li()

switch = []
for _ in range(m):
    s = list(li_())
    switch.append(s[1:])

p = list(li())

ans = 0
ok = True

for bit in range(1<<n):
    ok = True
    for i, swi in enumerate(switch):
        flag = 0
        for swij in swi:
            if bit & (1<<swij):
                flag += 1

        if flag % 2 != p[i]:
            ok = False

    if ok:
        ans += 1

print(ans)
