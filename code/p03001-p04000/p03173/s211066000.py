import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()

a_array = na()
sum_array = [0]
slime = 0
for a in a_array:
    slime += a
    sum_array.append(slime)

INF = 10 ** 15
ans = [[INF] * N for _ in range(N)]


def solve(l, r):
    # print(l,r)
    if ans[l][r] != INF:
        return ans[l][r]
    if l == r:
        ans[l][r] = 0
        # print(l,r,ans[l][r])
        return 0
    slime_sum = sum_array[r+1] - sum_array[l]
    # print(l,r,"slime",slime_sum)
    for i in range(l, r):
        ans[l][r] = min(ans[l][r], solve(l, i) + solve(i+1, r) + slime_sum)
    # print(l,r,ans[l][r])
    return ans[l][r]


print(solve(0, N-1))
