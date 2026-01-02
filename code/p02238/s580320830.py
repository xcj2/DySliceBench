def readinput():
    n=int(input())
    nList=[]
    for _ in range(n+1):
        nList.append([])
    for _ in range(n):
        l=list(map(int,input().split()))
        nList[l[0]]=l[2:]
    return n,nList

WHITE=0
GRAY=1
BLACK=2
color=[]
d=[]
f=[]
_time=0

def dfs(u,nList):
    global color
    global d
    global f
    global _time

    S=[]

    if(color[u]==WHITE):
        S.append(u)
        color[u]=GRAY
        _time+=1
        d[u]=_time

    while(len(S)>0):
        u=S[-1]
        t=next(u,nList)
        if(t!=-1):
            if(color[t]==WHITE):
                S.append(t)
                color[t]=GRAY
                _time+=1
                d[t]=_time
        else:
            S.pop()
            color[u]=BLACK
            _time+=1
            f[u]=_time

def next(u,nList):
    global color
    for t in nList[u]:
        if color[t]==WHITE:
            return t
    else:
        return -1

def main(n,nList):
    global color
    global d
    global f

    color=[WHITE]*(n+1)
    d=[0]*(n+1)
    f=[0]*(n+1)

    for i in range(1,n+1):
        dfs(i,nList)
    for i in range(1,n+1):
        print('{} {} {}'.format(i,d[i],f[i]))

if __name__=='__main__':
    n,nList=readinput()
    main(n,nList)

