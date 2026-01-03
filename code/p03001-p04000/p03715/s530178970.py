import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

H,W = LI()

if H%3 == 0 or W%3 == 0:
    print(0)
    exit()

ans = min(H,W)
for i in range(H):
    num1 = W*i
    num2 = math.floor(W/2)*(H-i)
    num3 = math.ceil(W/2)*(H-i)
    now = max(num1,num2,num3)-min(num1,num2,num3)
    if now < ans:
        ans = now

for i in range(W):
    num1 = H*i
    num2 = math.floor(H/2)*(W-i)
    num3 = math.ceil(H/2)*(W-i)
    now = max(num1,num2,num3)-min(num1,num2,num3)
    if now < ans:
        ans = now

print(ans)