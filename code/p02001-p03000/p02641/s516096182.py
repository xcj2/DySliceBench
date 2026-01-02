import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
X, N = mi()
A = li()

flag = [0] * (205)

for num in A:
    flag[num] = 1

if not flag[X]:
    print(X)
    exit()

i = 1
while True:
    if not flag[X - i]:
        print(X-i)
        exit()
    elif not flag[X + i]:
        print(X+i)
        exit()
    i += 1