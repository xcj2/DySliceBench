# coding:utf-8

import sys
import itertools

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
S = [c == 'o' for c in SI()]
S += S[:2]

SW = {'S': 'W', 'W': 'S'}
for a1, a2 in itertools.product('SW', repeat=2):
    M = [a1, a2]
    for i in range(n):
        if S[i + 1]:
            M.append(M[-2] if M[-1] == 'S' else SW[M[-2]])
        else:
            M.append(M[-2] if M[-1] == 'W' else SW[M[-2]])

    if M[0] == M[-2] and M[1] == M[-1]:
        print(*M[:-2], sep='')
        exit()

print(-1)
