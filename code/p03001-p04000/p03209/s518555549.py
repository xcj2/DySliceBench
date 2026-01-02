import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def POW(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return POW(x, y // 2) ** 2 % MOD
    else:
        return POW(x, y // 2) ** 2 * x % MOD
def mod_factorial(x, y): return x * POW(y, MOD - 2) % MOD
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import Counter

patis = [INF] * 51
layers = [INF] * 51
patis[0] = layers[0] = 1

def calc_layers(n):
    if layers[n] == INF:
        layers[n] = 3 + calc_layers(n - 1) * 2
    return layers[n]
calc_layers(50)

def calc_patis(n):
    if patis[n] == INF:
        patis[n] = 1 + calc_patis(n - 1) * 2
    return patis[n]
calc_patis(50)

def dfs(n, x):
    if layers[n] <= x:
        return patis[n], x - layers[n]
    ret = 0
    x -= 1
    if x <= 0:
        return ret, 0
    r, x = dfs(n - 1, x)
    ret += r
    if x <= 0:
        return ret, 0
    x -= 1
    ret += 1
    if x <= 0:
        return ret, 0
    r, x = dfs(n - 1, x)
    ret += r
    if x <= 0:
        return ret, 0
    x -= 1
    ret += 1
    return ret, x

def main():
    N, X = LI()
    ans, _ = dfs(N, X)
    return ans

print(main())