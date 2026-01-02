# ABC129 D

H,W=map(int,input().split())
S=[input() for _ in [0]*H]
Lx=[[0]*W for _ in [0]*H]
Ly=[[0]*W for _ in [0]*H]

def search_x(x,y):
    i=x
    while 1:
        i+=1
        if i<W:
            if S[y][i]=='#':
                break
        else:
            break
    return i-x

def search_y(x,y):
    j=y
    while 1:
        j+=1
        if j<H:
            if S[j][x]=='#':
                break
        else:
            break
    return j-y

def set_x(x,y,p):
    i=x
    Lx[y][i]=p
    while 1:
        i+=1
        if i<W:
            if S[y][i]=='#':
                break
            else:
                Lx[y][i]=p
        else:
            break

def set_y(x,y,p):
    j=y
    Ly[j][x]=p
    while 1:
        j+=1
        if j<H:
            if S[j][x]=='#':
                break
            else:
                Ly[j][x]=p
        else:
            break

res=0
for y in range(H):
    for x in range(W):
        if S[y][x]=='.':
            if Lx[y][x]==0:
                w=search_x(x,y)
                set_x(x,y,w)
            if Ly[y][x]==0:
                Ly[y][x]==0
                h=search_y(x,y)
                set_y(x,y,h)
            res=max(Lx[y][x]+Ly[y][x]-1,res)
print(res)