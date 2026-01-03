import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


w, h, n = LI()
ws = list(range(w + 1))
hs = list(range(h + 1))
for _ in range(n):
    x, y, a = LI()
    if a == 1:
        ws = [i for i in ws if x <= i]
    elif a == 2:
        ws = [i for i in ws if i <= x]
    elif a == 3:
        hs = [i for i in hs if y <= i]
    else:
        hs = [i for i in hs if i <= y]
if len(ws) == 0 or len(hs) == 0:
    ans = 0
else:
    ans = (ws[-1] - ws[0]) * (hs[-1] - hs[0])
print(ans)
