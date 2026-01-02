from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
def S(): return stdin.readline().rstrip()
def LI(): return list(map(int,stdin.readline().rstrip().split()))

def BFS(table,s,step,next,w,h):
    if table[h-1][w-1] != -2:
        return
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    nnext = []
    for rep in next:
        for j in range(4):
            nx = rep[0] + dx[j]
            ny = rep[1] + dy[j]
            if nx<0  or ny<0 or w<=nx or h<=ny:
                continue
            else:
                if s[ny][nx]=='#':
                    continue
                if table[ny][nx]==-2 or step+1<table[ny][nx]:
                    table[ny][nx] = step+1
                    nnext.append([nx,ny])
    if 0<len(nnext):
        BFS(table,s,step+1,nnext,w,h)

def main():
    tmp = LI()
    w,h = tmp.pop(),tmp.pop()
    s = [S() for _ in range(h)]
    table = [[-2]*w for _ in range(h)]
    BFS(table,s,0,[[0,0]],w,h)
    step = table[h-1][w-1]
    if step==-2:
        print(-1)
        exit()
    c = 0
    for rep in s:
        c += rep.count('#')
    ans = w*h-step-c-1
    print(ans)
    return

if __name__=='__main__':
    main()