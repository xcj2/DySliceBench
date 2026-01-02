import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

def calc_min(a, b):
    if a>=0 and b>=0:
        return a
    elif a<0 and b<0:
        return abs(b)
    else:
        return 0

N, K = mi()
x = li()
ans = 10**13 + 1
'''
sum_k = X[K-1] - X[0]
min_k = calc_min(x[0], x[K-1])
ans = sum_k
print(sum_k)
for i in range(1, N-K+1):
    sum_k -= abs(x[i-1]) + min_k
    sum_k += abs(x[K-1+i])
    min_k = calc_min(x[i], x[K-1+i])
    sum_k += min_k
    print(sum_k)
    ans = min(ans, sum_k)

print(ans)
'''

for i in range(N-K+1):
    #sum_k = x[K-1+i] - x[i] + calc_min(x[i], x[K-1+i])
    sum_k = x[K-1+i] - x[i] + min(abs(x[i]), abs(x[K-1+i]))
    #min_k = calc_min(N[i], N[K-1+i])
    #sum_k += min_k
    #print(sum_k)
    ans = min(ans, sum_k)

print(ans)


