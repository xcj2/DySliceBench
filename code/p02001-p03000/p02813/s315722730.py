# define
BIT = [0] * 20
frac = [1] * 20
ckn = [[0] * 20] * 20
maxN = 10
ans = [0] * 2

# BIT
def upd(pos, val) :
    i = pos
    while i <= maxN:
        BIT[i] += val
        i += (i & (-i))
def get(pos):
    res = 0
    i = pos
    while i > 0:
        res += BIT[i]
        i -= (i & (-i))
    return res
# calculation
def prepare():
    for i in range(1, maxN): frac[i] = frac[i - 1] * i
    for i in range(0, maxN):
        ckn[0][i] = 1
    for i in range(1, maxN):
        for j in range(i, maxN):
            ckn[i][j] = ckn[i - 1][j - 1] + ckn[i][j - 1]

# Main
prepare()
n = int(input())

for i in range(0, 2):
    for j in range(0, maxN): BIT[j] = 0
    s = input()

    for j in range(0, n) :
        x = int(s.split()[j])
        ans[i] += (x - 1 - get(x)) * frac[n - j - 1]
        upd(x, 1)

print(abs(ans[0] - ans[1]))
