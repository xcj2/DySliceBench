import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, K = na()
a_array = na()
mod = 10 ** 9 + 7

ans = [[0] * (K+1) for _ in range(N)]
total = [[0] * (K+1) for _ in range(N)]

for i in range(a_array[0]+1):
    ans[0][i] = 1
for i in range(K+1):
    total[0][i] = min(i + 1, a_array[0] + 1)


for i in range(1, N):
    for j in range(K+1):
        if j - a_array[i] > 0:
            ans[i][j] = (total[i-1][j] + mod - total[i-1]
                         [j-a_array[i]-1]) % mod
        else:
            ans[i][j] = total[i-1][j]
        if j == 0:
            total[i][j] = ans[i][j]
        else:
            total[i][j] = (total[i][j-1] + ans[i][j]) % mod


print(ans[-1][-1])
