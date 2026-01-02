import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

x,y,z,k = get_nums_l()

aaa = get_nums_l()
bbb = get_nums_l()
ccc = get_nums_l()

aaa.sort(reverse=True)
bbb.sort(reverse=True)
ccc.sort(reverse=True)

def solve(p):
    count = 0
    for a in aaa:
        for b in bbb:
            for c in ccc:
                if a+b+c < center:
                    break
                count += 1
                if count >= k:
                    return True
    return False

left = 0
right = 30000000001

while left+1 < right:
    center = (left + right) // 2

    if solve(center):
        left = center
    else:
        right = center

border = left

ans = []

for a in aaa:
    for b in bbb:
        for c in ccc:
            if a+b+c >= border:
                ans.append(a+b+c)
            else:
                break

ans.sort(reverse=True)
print("\n".join(list(map(str,ans[:k]))))
