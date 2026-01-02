def memorize(func):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper
def factorize(n, factor=2, index=0):
    counter = 0
    while True:
        if n%factor==0:
            n //=factor
            counter += 1
        else:
            break
    if counter>0:
        yield (factor, counter)
    if factor**2 < n:
        yield from factorize(n, factor+1)
    elif n>2:
        yield (n, 1)
@memorize
def choose(N, M):
    if M>N:
        return 0
    if N==0 or M==0:
        return 1
    else:
        return N*choose(N-1, M-1)//M
def ans(N, M):
    val = 1
    for _, r in factorize(M):
        val *= choose(N+r-1, r)
        val %= (10**9+7)
    return val
import sys; sys.setrecursionlimit(100000)
print(ans(*map(int, input().split())))