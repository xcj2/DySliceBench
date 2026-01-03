# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, K = MAP()
A = LIST()
INF = 10**20


def calc_cost(A, bit):
    cost = 0
    observed = 1
    prev_height = A[0]
    bit = bit | 1

    for n in range(1, N):
        if prev_height < A[n]:
            prev_height = A[n]
            observed += 1
        elif bit >> n & 1:
            costi = prev_height - A[n] + 1
            prev_height = A[n] + costi
            observed += 1
            cost += costi
    return observed, cost


ans = INF
for i in range(1 << N):
    observed, cost = calc_cost(A, i)
    if observed >= K:
        ans = min(ans, cost)

print(ans)


# for i in range(1 << N):
#     use = [i>>j & 1 for j in range(N)]
#     if sum(use) < K:
#         continue

#     res = 0
#     now = 