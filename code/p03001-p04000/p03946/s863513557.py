def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7

N, T = MI()
A = LMI()

# m[i] := i以降で最大の値
m = [0] * N
for j, a in enumerate(reversed(A)):
    if j == 0:
        m[N - 1] = a
        continue
    i = N - j - 1
    m[i] = max(a, m[i + 1])

M = 0
M_cnt = 0
for i, a in enumerate(A):
    if i == N - 1:
        continue
    diff = m[i + 1] - a
    if diff > M:
        M = diff
        M_cnt = 1
    elif diff == M:
        M_cnt += 1
print(M_cnt)
