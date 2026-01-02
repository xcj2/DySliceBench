# 5
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


n = I()
s = S()
ciphers = [f'{i:03}' for i in range(1000)]
ans = 0
for v in ciphers:
    j = 0
    for i in range(n):
        if s[i] == v[j]:
            j += 1
        if j == 3:
            ans += 1
            break
print(ans)
