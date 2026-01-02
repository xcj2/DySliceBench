import sys
from collections import deque

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,Q = LI()
str = S()
# l = [list(map(int,input().split())) for i in range(N)]

# 累積和
sum = list(range(N+1))
for i in range(N):
    if i+1<N and str[i] == 'A' and str[i+1] == 'C':
        sum[i+1] = sum[i] + 1
    else:
         sum[i+1] = sum[i]



for q in range(Q):
    l,r = LI()
    l -= 1
    r -= 1
    print(sum[r]-sum[l])