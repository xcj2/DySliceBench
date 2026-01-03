import sys
import math

INF = 10**9+7

stdin = sys.stdin
def na(): return map(int, stdin.readline().split())
def ns(): return stdin.readline().strip()
def nsl(): return list(stdin.readline().strip())
def ni(): return int(stdin.readline())
def nil(): return list(map(int, stdin.readline().split()))

n = ni()
a = nil()

ans = 1
c = a[0]
fg = 0
for i in range(1, n):
    if a[i] == c:
        c = a[i]
    elif a[i] > c :
        if fg == 1 or fg == 0:
            fg = 1
            c = a[i]
        else:
            ans += 1
            c = a[i]
            fg = 0
    else:
        if fg == -1 or fg == 0:
            fg = -1
            c = a[i]
        else:
            ans += 1
            c = a[i]
            fg = 0


print(ans)




