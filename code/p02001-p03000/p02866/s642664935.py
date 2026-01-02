import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = li()
max_num = 10**5+1
num_list = [0] * (max_num)

if A[0] != 0:
    print(0)
    exit()

for num in A:
    num_list[num] += 1

if num_list[0] > 1:
    print(0)
    exit()

ans = 1
for i in range(2, max_num):
    if num_list[i] != 0:
        ans *= pow(num_list[i-1], num_list[i], 998244353)

else:
    print(ans%998244353)