import bisect, functools, sys
sys.setrecursionlimit(10**6)
N = int(input())
A = sorted(int(x) for x in input().split())
B = sorted(int(x) for x in input().split())
C = sorted(int(x) for x in input().split())

@functools.lru_cache(maxsize=None)
def a(n):
    return bisect.bisect_left(A, n)

b_cache = [0] * (N + 1)
b_cached = [False] * (N + 1)
def b_i(i):
    global b_cache, b_cached
    if i >= 1:
        if not b_cached[i - 1]: b_i(i - 1)
        t = b_cache[i - 1] + a(B[i - 1])
        b_cache[i] = t
        b_cached[i] = True
        return t
    return 0

@functools.lru_cache(maxsize=None)
def b(n):
    return b_i(min(N, bisect.bisect_left(B, n)))

def c():
    return sum(b(x) for x in C)

print(c())