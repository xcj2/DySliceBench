from collections import deque

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

def main():
    H,W = ints_raw()
    DFST = [[-1 for i in range(W)]for i in range(H)]
    qu = deque()
    dirs = [[1,0,1],[0,1,1],[-1,0,1],[0,-1,1]]
    ans = 0
    for h in range(H):
        S = input()
        for w in range(W):
            if S[w]=="#":
                DFST[h][w]=0
                qu.append([h,w,0])
    while len(qu)!=0:
        cpos = qu.popleft()
        for dir in dirs:
            
            ny,nx,nt = [cpos[0]+dir[0],cpos[1]+dir[1],cpos[2]+dir[2]]
            if ny<0 or ny>=H or nx<0 or nx>=W:
                continue
            if DFST[ny][nx]!=-1:
                continue
            DFST[ny][nx]=nt
            ans = max(ans,nt)
            qu.append([ny,nx,nt])
    return ans

print(main())
