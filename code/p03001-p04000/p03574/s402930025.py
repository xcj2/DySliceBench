# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


h, w = LI()
M = [SI() for _ in range(h)]

d = ((0, 1), (-1, 1), (-1, 0), (-1, -1),
     (0, -1), (1, -1), (1, 0), (1, 1))

ans = []
for y in range(h):
    row = ''
    for x in range(w):
        cnt = 0
        if M[y][x] == '#':
            row += '#'
            continue

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < h and 0 <= xx < w:
                if M[yy][xx] == '#':
                    cnt += 1
        row += str(cnt)
    ans.append(row)

print(*ans, sep='\n')
