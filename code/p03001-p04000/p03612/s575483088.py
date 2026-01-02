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
p = LI()
inds = [i for i, j in enumerate(p) if i + 1 == j]
if len(inds) == 0:
    print(0)
else:
    ans = len(inds)
    counts = [1]
    cnt = 1
    for i in range(len(inds) - 1):
        if inds[i] + 1 == inds[i + 1]:
            counts[-1] += 1
        else:
            counts.append(1)
    for cnt in counts:
        ans -= cnt // 2
    print(ans)
