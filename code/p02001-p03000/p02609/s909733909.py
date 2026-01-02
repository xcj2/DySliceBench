import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
X = input()

popcount = X.count('1')

def mod(popcount):
    if popcount in [0, 1]:
        return [0] * N
    a = []
    base = 1
    for i in range(N):
        if i == 0:
            a.append(1)
        else:
            base = base * 2 % popcount
            a.append(base)
    return a

def summod(modX, popcount):
    if popcount == 0:
        return 0
    a = 0
    for i, x in enumerate(modX):
        if X[i] == '1':
            a = (a + x) % popcount
    return a

modXm = list(reversed(mod(popcount - 1)))
modXp = list(reversed(mod(popcount + 1)))

s_modXm = summod(modXm, popcount - 1)
s_modXp = summod(modXp, popcount + 1)

for i in range(N):
    if X[i] == '1':
        if popcount - 1 == 0:
            print(0)
            continue
        modX, s, m = modXm, s_modXm, popcount - 1
        s = (s + m - modX[i]) % m
    else:
        modX, s, m = modXp, s_modXp, popcount + 1
        s = (s + modX[i]) % m
    ans = 1
    while True:
        pc = bin(s).count('1')
        if pc == 0:
            break
        s = s % pc
        ans += 1
    print(ans)