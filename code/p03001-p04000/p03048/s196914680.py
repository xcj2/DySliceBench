# 26
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


R, G, B, N = LI()
ans = 0
for r in range(N + 1):
    for g in range(N + 1):
        bB = N - r * R - g * G
        b = bB // B
        if bB >= 0 and bB % B == 0 and R * r + G * g + B * b == N:
            # print(f'{(r, g, b)=}')
            ans += 1
print(ans)
