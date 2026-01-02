N, M = map(int, input().split())
A = list(map(int, input().split()))
cost = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
can_cost = sorted([cost[a] for a in A])
D = {}
for a in A:
    c = cost[a]
    D[c] = max(a, D.setdefault(c, -1))

min_cost = can_cost[0]
min_cost_num = D[min_cost]


def f2(v, l, num):
    L = list(str(v))
    min_cost = cost[int(num)]
    num = D.setdefault(min_cost + l, -1)
    if num == -1:
        return -1

    min_cost_num = D[min_cost]
    L[L.index(str(min_cost_num))] = str(num)
    L.sort(reverse=True)
    return int("".join(L))


def f(v, l):
    L = list(str(v))
    set_L = set(L)
    L2 = [f2(v, l, num) for num in set_L]
    return max(L2)

def g(K, r):
    temp = int("".join([str(min_cost_num)] * K))
    dp = [[-1 for _ in range(min(r, K) + 1)] for __ in range(r + 1)]
    dp[0][0] = temp

    for k in range(min(r, K)):
        for n in range(r):
            v = dp[n][k]
            if v == -1:
                continue
            for l in range(1, r - n + 1):
                dp[n + l][k + 1] = max(dp[n + l][k + 1], f(v, l))
    return max(dp[r])

K = N // min_cost
r = N - K * min_cost
res = g(K, r)
if g(K, r) == -1:
    res = g(K - 1, r + min_cost)
print(res)