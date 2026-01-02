import math
from functools import reduce

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,k = get_nums_l()
k -= 1
s = input()

ans = ""
for i in range(n):
    c = s[i]
    if i == k:
        ans += c.lower()
    else:
        ans += c

print(ans)