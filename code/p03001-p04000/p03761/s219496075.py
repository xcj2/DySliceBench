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
s = []

ans = []
x = 0
for i in range(n):
    s.append(nsl())
    s[i].sort()
    if(len(s[x]) > len(s[i])):
        x = i


for c in ''.join(s[x]):
    e = True
    while(e):
        for i in range(n):
            if(c not in s[i]):
                e = False
                break
            else:
                s[i].remove(c)
                if(i == n-1):
                    ans.append(c)

print(''.join(ans))



