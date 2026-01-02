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

N = I()

alpha = defaultdict(str)
for i in range(26):
    alpha[i] = chr(ord('a')+i)

# p桁でi+1番目に大きい
def calc(p,i):
    p -= 1
    ans = []
    while p >= 0:
        d = i//(26**p)
        ans.append(alpha[d])
        i -= (26**p)*d
        p -= 1
    return ''.join(ans)

c = 1
n = 0
while True:
    n += 26**c
    if n >= N:
        break
    else:
        c += 1

sum_ = 0
for i in range(1,c):
    sum_ += 26**i

print(calc(c,N-sum_-1))