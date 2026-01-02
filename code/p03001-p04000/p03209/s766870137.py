from functools import lru_cache

@lru_cache()
def f(n):
    if n==0:
        return 1
    return 2*f(n-1)+1

@lru_cache()
def g(n):
    if n==0:
        return 1
    return 2*g(n-1)+3

N, X = map(int, input().split())
total = [g(i) for i in range(N+1)]
p = [f(i) for i in range(N+1)]
ans = 0

def search(x, n):
    global ans
    if n==0:
        if x:
            ans += 1
        return
    if x==0:
        return
    if x > total[n-1] + 2:
        ans += p[n-1] + 1
        search(x-(2 + total[n-1]), n-1)
    elif x == total[n-1] + 2:
        ans += p[n-1] + 1
    else:
        search(x-1, n-1)

search(X, N)
print(ans)