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
 
def floor(a,b):
    return a//b

N,X,M = LI()

# 繰り返しの1回目が終わるまで
used = [-1]*M
end_index = -1
A = [X]
sum_ = 0
for i in range(N):
    if i == 0:
        sum_ += A[0]
    else:
        val = pow(A[i-1],2,M)
        A.append(val)
        if used[val] == -1:
            used[val] = i
            sum_ += val
        else:
            end_index = i
            start_val = val
            start_index = used[val]
            break

if end_index == -1:
    print(sum_)
    exit()
else:
    ans = sum_


# 繰り返し全体が終わるまで
n = floor(N-start_index,end_index-start_index)
sum_ = 0
A2 = [start_val]
for j in range(end_index-start_index):
    if j == 0:
        val2 = start_val
        sum_ += val2
    else:
        val2 = pow(A2[j-1],2,M)
        A2.append(val2)
        sum_ += val2

ans += (n-1)*sum_


# 残りの部分
sum_ = 0
A2 = [start_val]
for j in range(N-n*end_index+(n-1)*start_index):
    if j == 0:
        val2 = start_val
        sum_ += val2
    else:
        val2 = pow(A2[j-1],2,M)
        A2.append(val2)
        sum_ += val2

ans += sum_

print(ans)