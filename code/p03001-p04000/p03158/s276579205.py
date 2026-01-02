import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,Q = II()
A = III()
X = Line(Q,1)

if N==2:
    for _ in range(Q):
        print(A[-1])
    exit()

sum_list = [0]*N
now_odd = 0
now_even = 0
for i in range(N):
    if i%2==0:
        now_even += A[i]
        sum_list[i] = now_even
    else:
        now_odd += A[i]
        sum_list[i] = now_odd        

left_sum = [0]*N
now = 0
for i in range(N)[::-1]:
    now += A[i]
    left_sum[i] = now

for x in X:
    left = 0
    right = N//2
    while (right-left>1):
        mid = left + (right-left)//2
        if abs(A[N-mid-2]-x)<abs(A[N-2*mid-2]-x):
            right = mid
        else:
            left = mid
    right1 = right

    left = 0
    right = N//2 + 1
    while (right-left>1):
        mid = left + (right-left)//2
        if abs(A[N-mid-1]-x)<abs(A[N-2*mid-1]-x):
            right = mid
        else:
            left = mid
    right2 = right

    flag = False
    if right1 != right2:
        flag = True

    ans = left_sum[N-right2]

    if flag:
        if N-right1-right2-2>=0:
            ans += sum_list[N-right1-right2-2]
    else:
        if N-right1-right2-1>=0:
            ans += sum_list[N-right1-right2-1]
    print(ans)