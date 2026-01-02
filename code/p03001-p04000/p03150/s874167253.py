# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def SS(): return input()


S = SS()

key = 'keyence'
n = 0
j = 0
for l in range(-1, len(S)):
    for r in range(l, len(S)):
        n = 0
        j = 0
        # print(l, r)
        for i in range(len(S)):
            if l <= i <= r:
                continue
            # print(i, n)
            if n == len(key):
                j = 1
                break
            if S[i] == key[n]:
                n += 1
            else:
                break
        else:
            if n == len(key) and j == 0:
                print('YES')
                exit()

print('NO')
