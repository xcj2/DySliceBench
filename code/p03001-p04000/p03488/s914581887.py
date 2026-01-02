import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())+['T']
X, Y = mapint()
H = []
V = []

now_dirc = 1
cnt = 0
for s in S:
    if s=='F':
        cnt += 1
    else:
        if now_dirc==1:
            H.append(cnt)
        else:
            V.append(cnt)
        now_dirc*=-1
        cnt = 0

def check(now, goal, lis):
    dp = [0]*20000
    dp[10000+now] = 1
    for l in lis:
        nxdp = [0]*20000
        for i in range(20000):
            if i-l>=0 and dp[i-l]==1:
                nxdp[i] = 1
            if i+l<20000 and dp[i+l]==1:
                nxdp[i] = 1
        dp = nxdp
    if dp[goal+10000]:
        return True
    else:
        return False
    
if check(H[0], X, H[1:]) and check(0, Y, V):
    print('Yes')
else:
    print('No')