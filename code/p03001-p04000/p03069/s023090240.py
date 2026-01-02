import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
S = input()

blacks = S.count('#')
if blacks == 0:
    print(0)
    exit(0)

ans = blacks

# w[i] := i番目以降にいくつの白があるか
# b[i] := i番目より前にいくつの黒があるか
w = [0] * N
b = [0] * N
for i, c in enumerate(S):
    if i == 0:
        continue
    if S[i - 1] == '#':
        b[i] += 1
    if i < N - 1:
        b[i + 1] = b[i]
for i, c in enumerate(reversed(S)):
    i = N - i - 1
    if i == N - 1:
        if c == '.':
            w[i] = 1
        continue
    w[i] = w[i + 1]
    if c == '.':
        w[i] += 1


for i, c in enumerate(S):
    if c == '#':
        ans = min(ans, w[i] + b[i])

print(ans)
