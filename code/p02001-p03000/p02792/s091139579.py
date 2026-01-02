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

table = dp2(0, 10, 10)

for i in range(1, N+1):
    head = int(str(i)[0])
    tail = int(str(i)[-1])
    table[head][tail] += 1
#print(table)
cnt = 0
for i in range(10):
    for j in range(10):
        cnt += table[i][j] * table[j][i]
        #if i == j:
            #cnt += table[i][j]

print(cnt)