import sys

sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return [int(x) for x in input().split()]
MOD = 10**9 + 7

def comb(n, k):
    if n < k:
        return 0

    m = 1
    if n < 2 * k:
        k = n - k
    for i in range(1, k + 1):
        m = m * (n - i + 1) // i    
    return m

N = INT()

s = []

for _ in range(N):
    s.append(sorted(input()))

s = sorted(s)
s.append("")

ans = 0

i = 0
while i < N:
    j = i + 1

    while s[i] == s[j]:
        j += 1

    ans += comb(j - i, 2)

    i = j

print(ans)
