def solve(x):
    for i in a:
        x = i * (x // i)
    return x

def solve_min(c1, c2):
    m = (c1 + c2 + 1) // 2
    if abs(c1 - c2) <= 1:
        return m
    else:
        if solve(m) < 2:
            c1 = m
        else:
            c2 = m
        return solve_min(c1, c2)

def solve_max(c1, c2):
    m = (c1 + c2 + 1) // 2
    if abs(c1 - c2) <= 1:
        return m
    else:
        if solve(m) <= 2:
            c1 = m
        else:
            c2 = m
        return solve_max(c1, c2)

k = int(input())
a = list(map(int, input().split()))
maxa = max(a)
mi = solve_min(maxa - 1, pow(10, 18))
ma = solve_max(maxa - 1, pow(10, 18))
ans = [mi, ma - 1]
print(-1 if mi == ma else " ".join(map(str, ans)))