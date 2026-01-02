DVSR = 998244353
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def II(): return int(input())

N = int(input())
INL = [II() for _ in range(N)]
SM = sum(INL)
HSM = SM//2

DP1 = [[0]*(SM+1) for _ in range(N+1)]
DP2 = [[0]*(SM+1) for _ in range(N+1)]
DP1[0][0] = 1
DP2[0][0] = 1

for i, value in enumerate(INL, 1):
    for j in range(SM+1):
        if j-value >= 0:
            DP1[i][j] = (2*DP1[i-1][j]+DP1[i-1][j-value])%DVSR
            DP2[i][j] = (DP2[i-1][j]+DP2[i-1][j-value])%DVSR
        else:
            DP1[i][j] = (2*DP1[i-1][j])%DVSR
            DP2[i][j] = DP2[i-1][j]

sub = 0
patall = POW(3, N)
for i in range(HSM+1, SM+1):
    sub += DP1[N][i]*3

if SM % 2 == 0:
    sub += 3*(DP1[N][HSM] - 2*DP2[N][HSM])
    sub += 3*DP2[N][HSM]

# print(DP2[N])
# print(SM)
print((patall - sub) % DVSR)