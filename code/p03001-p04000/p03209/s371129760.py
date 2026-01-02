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

N, X = mi()

def rec(level, pos, score):
    #print(level, pos, score)
    if level == 0:
        return score + 1
    half = 2**(level+1) - 2
    if pos == 0:
        return score
    elif pos == half * 2:
        return score + 2**(level+1) - 1
    elif pos == half:
        return score + 2**(level)
    elif pos > half:
        score += 2**(level)
        pos -= half + 1
    else:
        pos -= 1
    return rec(level-1, pos, score)
    
X -= 1
print(rec(N, X, 0))