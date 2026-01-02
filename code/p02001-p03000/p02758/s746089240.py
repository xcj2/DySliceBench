from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

MOD = 998244353

n = int(input())
robot = []
pos = []

for i in range(n):
    x, d = map(int, input().split())
    robot.append([x, x+d])
    pos.append(x)

robot = sorted(robot, key=lambda y: y[0])
pos = sorted(pos)


def init(init_val):
    for i in range(n):
        MI[i+num-1] = init_val[i]
        MA[i+num-1] = init_val[i]
    for i in range(num-2, -1, -1):
        MI[i] = min(MI[2*i+1], MI[2*i+2])
        MA[i] = max(MA[2*i+1], MA[2*i+2])


def update(k, x):
    k += num-1
    MI[k] = x
    MA[k] = x
    while k+1:
        k = (k-1)//2
        MI[k] = min(MI[k*2+1], MI[k*2+2])
        MA[k] = max(MA[k*2+1], MA[k*2+2])


def rangemax(p, q):
    if q <= p:
        return -1
    p += num-1
    q += num-2
    res = -1
    while q-p > 1:
        if p & 1 == 0:
            res = max(res, MA[p])
        if q & 1 == 1:
            res = max(res, MA[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res, MA[p])
    else:
        res = max(max(res, MA[p]), MA[q])
    return res


# n:リスト長
num = 2**(n-1).bit_length()
MI = [1 << 100]*2*num
MA = [-1]*2*num

r = []
for x, d in robot:
    r.append(bisect_left(pos, d))

init(r)

s = [0]*n

for x in range(n-1, -1, -1):
    right_max = rangemax(x, r[x])
    s[x] = right_max
    update(x, right_max)

dp = [0]*(n+1)
dp[-1] = 1

for i in range(n-1, -1, -1):
    dp[i] = dp[i+1]+dp[s[i]]
    dp[i] %= MOD

print(dp[0])
