import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
M = [list(str(input())) for _ in range(H)]

cnt = 0
for i in range(H):
    for j in range(W):
        if M[i][j]=="#":
            cnt += 1
if cnt!=H+W-1:
    print("Impossible")
else:
    def dfs(x, y):
        if x==W-1 and y==H-1:
            return 1
        ret = 0
        if x+1<W and M[y][x+1]=='#':
            ret += dfs(x+1, y)
        if y+1<H and M[y+1][x]=="#":
            ret += dfs(x, y+1)
        return ret
    
    if dfs(0, 0)>0:
        print('Possible')
    else:
        print('Impossible')