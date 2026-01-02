import math
import string
import collections
from collections import Counter


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())
a = readints()
# print(a)
c = Counter(a)  # リストの各要素の出現回数をカウント
# print(c)
cnt = 0
# print(c.values())
for i in c.values():
    # 各要素の値に対してforループ処理
    cnt += i*(i-1)//2
for aa in a:
    x = c[aa]
    # print(x)
    ans = (cnt-x*(x-1)//2+(x-1)*(x-2)//2)
    print(ans)
