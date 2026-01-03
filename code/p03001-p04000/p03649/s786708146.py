import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

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

# 操作：c回と固定すると，
# 各要素を何回以上選ぶ必要があるかわかる
# c→c+(N+1) とすると，必要回数の和が+Nになることから，
# 最小のc(mod N+1)がわかる

def ceil(x,y):
    return x//y + int(x%y != 0)

N = I()
a = LI()

ans = float('inf')
for c in range(N+1):
    need = 0
    for i in range(N):
        need += max(0,ceil(c+a[i]-(N-1),N+1))
    if need <= c:
        temp = c
    else:
        temp = c+(need-c)*(N+1)
    if temp < ans:
        ans = temp

print(ans)