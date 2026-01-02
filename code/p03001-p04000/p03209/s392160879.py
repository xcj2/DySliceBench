N, X = map(int, input().split())

def a(L):
    if L == 0:
        return 1
    return 2 * a(L-1) + 3

def p(L):
    if L == 0:
        return 1
    return 2 * p(L-1) + 1

def solve(L, X):
    if L == 0:
        return 0 if X == 0 else 1
    if X == 1:
        return 0
    if 1 < X <= 1 + a(L-1):
        return solve(L-1, X-1)
    if X == 2 + a(L-1):
        return p(L-1) + 1
    if 2 + a(L-1) < X <= 2 + 2 * a(L-1):
        return p(L-1) + 1 + solve(L-1, X-a(L-1)-2)
    if X == 3 + 2 * a(L-1):
        return 2 * p(L-1) + 1

print(solve(N, X))