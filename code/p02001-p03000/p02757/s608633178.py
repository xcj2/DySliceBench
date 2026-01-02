n, p = map(int, input().split())
s = list(map(int, list(input())))

u = [ 0 for i in range(n+1)]

d = 1
for i in range(n):
    u[n-(i+1)] = (u[n-i] + s[n-1-i] * d) % p
    d = 10 * d % p

# print(u, d)

def solve(u, s):
    if p == 2 or p == 5:
        return solve1(s)
    else:
        return solve2(u)


def solve1(s):
    ans = 0
    for i in range(n):
        if s[i] % p == 0:
            ans += i+1
    return ans

def solve2(u):
    ans = 0
    cnt = [0 for i in range(p)]
    for i in range(n+1):
        cnt[u[i]] += 1
    for i in range(p):
        q = cnt[i]
        ans += (q * (q-1)) // 2
    return ans

print(solve(u, s))

