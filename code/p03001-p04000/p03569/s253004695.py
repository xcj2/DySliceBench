import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

s = list(input())
ans = 0
left = 0
right = len(s)-1

while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    elif s[left] == 'x':
        ans += 1
        left += 1
    elif s[right] == 'x':
        ans += 1
        right -= 1
    else:
        print(-1)
        exit()

print(ans)