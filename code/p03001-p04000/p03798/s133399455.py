# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
s = SI()

s = s[-1] + s + s[0]
P = ('00', '01', '10', '11')  # 0: S, 1: W
for p in P:
    for i in range(1, n):
        # print(i, p[-1], s[i])
        if s[i + 1] == 'o':
            p += p[-2] if p[-1] == '0' else str(int(p[-2]) ^ 1)
        else:
            p += p[-2] if p[-1] == '1' else str(int(p[-2]) ^ 1)
    else:
        if s[1] == 'o':
            tmp = p[1] if p[0] == '0' else str(int(p[1]) ^ 1)
        else:
            tmp = p[1] if p[0] == '1' else str(int(p[1]) ^ 1)
        p = tmp + p

    if p[1] == p[-1] and p[-2] == p[0]:
        ans = ''
        for a in p[1:-1]: ans += 'S' if a == '0' else 'W'
        print(ans)
        exit()

print(-1)
