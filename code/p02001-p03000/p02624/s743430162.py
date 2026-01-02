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

def sieve(n):
    count = [1 for i in range(n+1)]
    count[0] = 0

    for i in range(1, n+1):
        j = 2 * i
        while j <= n:
            count[j] += 1
            j += i
    return count

N = ii()
l = sieve(N)

print(sum([l[i] * i for i in range(1, N+1)]))