import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
a = []
b = []
for _ in range(n):
    ai, bi = LI()
    a.append(ai)
    b.append(bi)
p = 0
for ai, bi in zip(a[::-1], b[::-1]):
    ai += p
    if ai % bi == 0:
        continue
    elif bi > ai:
        p += bi - ai
    else:
        p += bi - (ai % bi)
print(p)
