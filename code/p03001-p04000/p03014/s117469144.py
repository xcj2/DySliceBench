import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

H,W=LI()
MP=[input() for _ in range(H)]

mp_wid=[[0]*W for _ in range(H)]
mp_hei=[[0]*W for _ in range(H)]

for i in range(H):
    cnt = 0
    for j in range(W):
        if MP[i][j] == '.':
            cnt += 1
        else:
            for k in range(cnt):
                mp_wid[i][j-k-1] = cnt
            cnt=0
    for k in range(cnt):
        mp_wid[i][-k-1] = cnt

for j in range(W):
    cnt = 0
    for i in range(H):
        if MP[i][j] == '.':
            cnt+=1
        else:
            for k in range(cnt):
                mp_hei[i-k-1][j] = cnt
            cnt=0
    for k in range(cnt):
        mp_hei[-k-1][j] = cnt

# for li in mp_wid:
#     print(li)
# print('')
# for li in mp_hei:
#     print(li)
res = 0
for i in range(H):
    for j in range(W):
        res = max(res, mp_hei[i][j]+mp_wid[i][j]-1)
print(res)
