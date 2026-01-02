import sys
# gcd
# from fractions import gcd
# 切り上げ，切り捨て
# from math import ceil, floor
# リストの真のコピー（変更が伝播しない）
# from copy import deepcopy
# 累積和。list(accumulate(A))としてAの累積和
# from itertools import accumulate
# l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# S = Counter(l)  # カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
# print(S.most_common(2))  # [('b', 5), ('c', 4)]
# print(S.keys())  # dict_keys(['a', 'b', 'c'])
# print(S.values())  # dict_values([3, 5, 4])
# print(S.items())  # dict_items([('a', 3), ('b', 5), ('c', 4)])
# from collections import Counter
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


N = ii()
S = li()
K = ii()
st = S[K-1]
for i in range(N):
    if S[i] != st:
        S[i] = '*'

print(''.join(S))