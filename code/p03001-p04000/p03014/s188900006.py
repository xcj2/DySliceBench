#ABC129-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
h,w=IL()
G=[S() for i in range(h)]
V=[[0]*w for i in range(h)]
H=[[0]*w for i in range(h)]
c=0
for i in range(h):
    for j in range(w):
        if G[i][j]=="#":
            for k in range(c):
                H[i][j-k-1]=c
            c=0
        elif j==w-1:
            c+=1
            for k in range(c):
                H[i][j-k-1]=c
            c=0
        else:
            c+=1
            
for i in range(w):
    for j in range(h):
        if G[j][i]=="#":
            for k in range(c):
                V[j-k-1][i]=c
            c=0
        elif j==h-1:
            c+=1
            for k in range(c):
                V[j-k-1][i]=c
            c=0
        else:
            c+=1

ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,V[i][j]+H[i][j]-1)
print(ans)