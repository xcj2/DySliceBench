import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
S = LS2()

from collections import defaultdict

d_left = defaultdict(int)
d_right = defaultdict(int)

for i in range(2**N):
    left_red = ''
    left_blue = ''
    right_red = ''
    right_blue = ''
    for j in range(N):
        if (i >> j) & 1:
            left_red += S[j]
        else:
            left_blue += S[j]
    for j in range(2*N-1,N-1,-1):
        if (i >> (j-N)) & 1:
            right_red += S[j]
        else:
            right_blue += S[j]
    d_left[(left_red,left_blue)] += 1
    d_right[(right_red,right_blue)] += 1

ans = 0
for key in d_left.keys():
    ans += d_left[key]*d_right[key]

print(ans)
