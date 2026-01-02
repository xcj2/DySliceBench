import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
from itertools import accumulate #list(accumulate(A))

N, K = mi()
S = input()

len_list = []
ind = 0
if S[0] == '0':
    #len_list[0] = 0
    len_list.append(0)
    #ind += 1

cnt = 1
for i in range(1, N):
    if S[i] != S[i-1]:
        #len_list[ind] = cnt
        len_list.append(cnt)
        #ind += 1
        cnt = 1
    else:
        cnt += 1
#len_list[ind] = cnt
len_list.append(cnt)

l_list = len(len_list)
wa = [0] + list(accumulate(len_list))
ans = 0
i = 1
l_wa = len(wa)
while True:
    if i+2*K >= l_wa:
        ans = max(ans, wa[l_wa-1] - wa[i-1]) 
        break
    #if i == 0:
        #ans = wa[i+2*K+1]
    ans = max(ans, wa[i+2*K] - wa[i-1]) 
    i += 2
print(ans)