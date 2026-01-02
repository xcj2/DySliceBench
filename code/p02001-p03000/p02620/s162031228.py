import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


D = I()
C = LMI()
S = [LMI() for _ in range(D)]
T = [I() - 1 for _ in range(D)]
M = I()

last = [[i + 1] * 26 for i in range(D)]
for d in range(D):
    i = T[d]
    j = 0
    for dd in range(d, D):
        last[dd][i] = j
        j += 1

def eval(d, q):
    i = T[d]
    val = S[d][q] - S[d][i]

    contrib = 0
    if d == 0:
        j = 1
    else:
        j = last[d - 1][i] + 1
    for dd in range(d, D):
        if dd > d and last[dd][i] == 0:
            break
        contrib += j - last[dd][i]
        last[dd][i] = j
        j += 1
    val -= contrib * C[i]

    contrib = 0
    j = 0
    for dd in range(d, D):
        if last[dd][q] == 0:
            break
        contrib += last[dd][q] - j
        last[dd][q] = j
        j += 1
    val += contrib * C[q]

    T[d] = q

    return val


def score0(T):
    last = defaultdict(int)
    ans = 0
    for d in range(D):
        ans += S[d][T[d]]
        last[T[d]] = d + 1
        for i in range(26):
            ans -= C[i] * (d + 1 - last[i])
    return ans


score = score0(T)
for d, q in [tuple(MI0()) for _ in range(M)]:
    val = eval(d, q)
    score += val
    print(score)