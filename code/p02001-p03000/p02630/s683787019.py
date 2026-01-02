import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

from collections import Counter

N = I()
A = LI()
sum = sum(A)
a = Counter(A)

Q = I()
for i in range(Q):
    b,c = LI()
    sum += a[b]*(c-b)
    print(sum)
    a[c] += a[b]
    a[b] = 0