import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math

n, q = getList()

vtxs = [[] for i in range(n)]
already = [0 for i in range(n)]

for i in range(n - 1):
    a, b = getList()
    vtxs[a-1].append(b -1)
    vtxs[b-1].append(a - 1)

count = [0 for i in range(n)]
for i in range(q):
    x, v = getList()
    count[x-1] += v

ans = [0 for i in range(n)]

def rep(vx, val):
    # print(vx,val)
    tgt = vtxs[vx]
    already[vx] = 1
    for tg in tgt:
        if already[tg] == 0:
            app = count[tg]
            ans[tg] = val+app
            rep(tg, val+app)

rep(0, count[0])
# print(vtxs)
ans[0] = count[0]
print(*ans)
