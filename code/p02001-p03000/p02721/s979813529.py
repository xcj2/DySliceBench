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

N,K,C = LI()
S = list(input())

# oの日
ok = []
for i in range(N):
    if S[i] == 'o':
        ok.append(i)

# 順方向で何日働けるか
dp = [0]*N
dp[0] = 1 if S[0] == 'o' else 0
for i in range(1,N):
    if S[i] == 'o':
        if dp[i-1] == 0:
            dp[i] = 1
        else:
            if i-C-1 >= 0:
                dp[i] = max(dp[i-1],dp[i-C-1]+1)
            else:
                dp[i] = max(dp[i-1],1)
    else:
        dp[i] = dp[i-1]

# 逆方向で何日働けるか
dp2 = [0]*N
dp2[-1] = 1 if S[-1] == 'o' else 0
for i in range(N-1)[::-1]:
    if S[i] == 'o':
        if dp2[i+1] == 0:
            dp2[i] = 1
        else:
            if i+C+1 <= N-1:
                dp2[i] = max(dp2[i+1],dp2[i+C+1]+1)
            else:
                dp2[i] = max(dp2[i+1],1)
    else:
        dp2[i] = dp2[i+1]

# 左右から貪欲をしたときに用いる日
left = []
right = []
now = 0
for i in range(N):
    if dp[i] != now:
        left.append(i)
        now += 1
now = 0
for i in range(N)[::-1]:
    if dp2[i] != now:
        right.append(i)
        now += 1
right = list(reversed(right))

# 次に働ける直近の日
ne = [-1]*N
for i in range(N):
    if S[i] == 'o':
        p = bisect_left(ok,i+C+1)
        if p < len(ok):
            ne[i] = ok[p]

# 次にoが来る日
neo = [-1]*N
for i in range(N):
    if S[i] == 'o':
        p = bisect_left(ok,i+1)
        if p < len(ok):
            neo[i] = ok[p]

ans = []
for i in range(N):
    p1 = bisect_right(left,i-1)-1
    p2 = bisect_left(right,i+1)
    if p1 == -1:
        if p2 == len(right):
            num = 0
        else:
            num = dp2[right[p2]]
    else:
        if p2 == len(right):
            num = dp[left[p1]]
        else:
            v1 = left[p1]
            v2 = right[p2]
            if v1 == v2:
                num = dp[v1]+dp2[v2]-1
            elif v2-v1 >= C+1:
                num = dp[v1]+dp2[v2]
            else:
                nex = ne[v1]
                if nex == -1:
                    num = dp[v1]
                elif nex == i:
                    right = neo[nex]
                    if right == -1:
                        num = dp[v1]
                    else:
                        num = dp[v1]+dp2[right]
                else:
                    num = dp[v1]+dp2[nex]
    if num < K:
        ans.append(i)

for a in ans:
    print(a+1)