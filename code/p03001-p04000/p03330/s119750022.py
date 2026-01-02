import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N, C = mi()
D = li2(C)
S = li2(N)

table = dp2(0, C, 3)
'''
#for num in range(3):
    #for start in range(num, N, 3):
        for color in range(C):
            i = 0
            j = start
            print(i, j)
            while True:
                table[num][color] += D[S[i][j]-1][color]
                if j < 1 or i >= N:
                    break
                j -= 1
                i += 1
'''
for i in range(N):
    for j in range(N):
        for color in range(C):
            table[(i+j)%3][color] += D[S[i][j]-1][color]

ans = float('inf')
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or k == i:
                continue
            ans = min(ans, table[0][i] + table[1][j] + table[2][k])

print(ans)