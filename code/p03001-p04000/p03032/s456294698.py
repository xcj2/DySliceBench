import math
from functools import reduce
from collections import deque

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,k = get_nums_l()
v = get_nums_l()

# 左側でpos回操作するときの最大得点
left = [0]*(k+1)
leftmark = [0]*(k+1)
# 右側
right = [0]*(k+1)

for i in range(1,k+1):
    score = max(left[i-1], sum(v[:i]))
    leftmark[i] = i
    for ii in range(i//2):
        ii += 1
        score_ = sum(sorted(v[:i-ii],reverse=True)[:i-(ii*2)])
        if score_ > score:
            score = score_
            leftmark[i] = i-ii
    left[i] = score

for i in range(1,k+1):
    score = max(right[i-1],sum(v[max(leftmark[k-i],(n-i)):]))
    for ii in range(i//2):
        ii += 1
        score = max(score, sum(sorted(v[max(leftmark[k-i],n-i+ii):],reverse=True)[:min(n-leftmark[k-i], i-(ii*2))]))
    right[i] = score

ans = 0

for i in range(k+1):
    ans = max(ans, left[i] + right[k-i])
print(ans)