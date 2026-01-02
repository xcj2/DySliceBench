def readinput():
    h,w=map(int,input().split())
    smat=[]
    for _ in range(h):
        smat.append(input())
    return h,w,smat

def main(h,w,smat):
    tmat=[]
    for _ in range(h):
        t=[0 for tt in range(w)]
        tmat.append(t)
    #print(tmat)
    for i in range(h):
        s=smat[i]
        l=0
        r=s.find('#',l)
        #print(i,l,r)
        while(r>=0):
            for k in range(l,r):
                tmat[i][k]=r-l
            l=r+1
            if (l>=w):
                break
            r=s.find('#',l)
            #print(i,l,r)
        else:
            for k in range(l,w):
                tmat[i][k]=w-l
        #print(tmat[i])
    maxt=0
    for j in range(w):
        u=0
        b=u
        while b<h:
            #print(b,j)
            while b<h and smat[b][j]=='.':
                b+=1
            for k in range(u,b):
                maxt=max(maxt, tmat[k][j]+b-u-1)
            u=b+1
            b=u

    return maxt

def main2(h,w,smat):
    l=[]
    r=[]
    u=[]
    d=[]
    for _ in range(h):
        l.append([0]*w)
        r.append([0]*w)
        u.append([0]*w)
        d.append([0]*w)

    for i in range(h):
        for j in range(w):
            if smat[i][j]=='.':
                if j==0:
                    l[i][j]=1
                else:
                    l[i][j]=l[i][j-1]+1
        for j in range(w-1,-1,-1):
            if smat[i][j]=='.':
                if j==w-1:
                    r[i][j]=1
                else:
                    r[i][j]=r[i][j+1]+1
    for j in range(w):
        for i in range(h):
            if smat[i][j]=='.':
                if i==0:
                    u[i][j]=1
                else:
                    u[i][j]=u[i-1][j]+1
        for i in range(h-1,-1,-1):
            if smat[i][j]=='.':
                if i==h-1:
                    d[i][j]=1
                else:
                    d[i][j]=d[i+1][j]+1
    
    maxt=0
    for i in range(h):
        for j in range(w):
            maxt=max(maxt, l[i][j]+r[i][j]+u[i][j]+d[i][j]-3)
    return maxt

if __name__=='__main__':
    h,w,smat=readinput()
    ans=main2(h,w,smat)
    print(ans)
