import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def solve():
    dp0 = [0] * (w + 1)
    dp1 = [0] * (w + 1)
    dp2 = [0] * (w + 1)
    dp3 = [0] * (w + 1)
    for i in range(h):
        for j in range(w):
            v = vv[i * w + j]
            if v:
                dp3[j] = max(dp3[j], dp2[j] + v)
                dp2[j] = max(dp2[j], dp1[j] + v)
                dp1[j] = max(dp1[j], dp0[j] + v)
            dp3[j + 1] = max(dp3[j + 1], dp3[j])
            dp2[j + 1] = max(dp2[j + 1], dp2[j])
            dp1[j + 1] = max(dp1[j + 1], dp1[j])
            dp0[j] = max(dp1[j], dp2[j], dp3[j])
    print(dp0[-2])

h, w, k = MI()
vv = [0] * h * w
for _ in range(k):
    i, j, v = MI()
    i, j = i - 1, j - 1
    vv[i * w + j] = v
solve()
