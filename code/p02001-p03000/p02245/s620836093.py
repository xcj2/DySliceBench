N = 3
dx = [0,-1,0,1]
dy = [1,0,-1,0]
limit = 0
t = [[0 for i in range(N)] for j in range(N)]

def getH():
    sum = 0
    x = int(0)
    for i in range(N):
        for j in range(N):
            if t[i][j]==0:continue
            x=t[i][j]-1
            sum += abs(int(x/N)-i)+abs((int(x%N)-j))
    return sum

def dfs( depth, prev,py,px):
    h=getH()
    if h == 0 :return True 
    if depth+h > limit: return False
    for i in range(4):
        if abs(i-prev) == 2 : continue
        tx=px+dx[i]
        ty=py+dy[i]
        if tx<0 or ty<0 or tx>=N or ty>=N:continue
        t[ty][tx],t[py][px] = t[py][px],t[ty][tx]
        if dfs(depth+1,i,ty,tx) :return True
        t[ty][tx],t[py][px] = t[py][px],t[ty][tx]
    return False

def Solve(py, px):
    global limit
    limit =0
    while True:
        if dfs(0,99,py,px):
            print(limit)
            return 
        limit += 1
 
if __name__=='__main__':
    for i in range(N):
        tmp =list(map(int, input().split()))
        for j in range(N):
            t[i][j]=tmp[j]
            if t[i][j]==0:
                py=i
                px=j
    Solve(py,px)


