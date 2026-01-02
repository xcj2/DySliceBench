import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
S = LI()
q = I()
T = LI()
ans = 0
for t in T:
    a = 0
    for i in range(1, 10 * math.ceil(math.log(2, n)) + 10):
        if S[a] == t:
            ans += 1
            break
        elif S[a] < t:
            a += math.ceil(n / pow(2, i))
            if a >= n - 1:
                a = n - 1
        else:
            a -= math.ceil(n / pow(2, i))
            if a <= 0:
                a = 0
print(ans)

