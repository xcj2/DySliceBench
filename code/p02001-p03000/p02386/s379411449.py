d=[(0,0,1),(-1,0,0),(0,1,0),(0,-1,0),(1,0,0),(0,0,-1)]
def crosspro(y,x):
    return (y[1]*x[2]-y[2]*x[1],y[2]*x[0]-y[0]*x[2],y[0]*x[1]-y[1]*x[0])
def north(r):
    res=[]
    for p in r:
        res.append((p[2],p[1],-p[0]))
    return res
def south(r):
    res=[]
    for p in r:
        res.append((-p[2],p[1],p[0]))
    return res
def east(r):
    res=[]
    for p in r:
        res.append((p[0],p[2],-p[1]))
    return res
def west(r):
    res=[]
    for p in r:
        res.append((p[0],-p[2],p[1]))
    return res
def left(r):
    res=[]
    for p in r:
        res.append((p[1],-p[0],p[2]))
    return res
def right(r):
    res=[]
    for p in r:
        res.append((-p[1],p[0],p[2]))
    return res
T=["","N","E","W","S","NN"]
U=["","L","LL","LLL"]
def change(S):
    D=d
    for i in S:
        if i=="N":
            D=north(D)
        elif i=="E":
            D=east(D)
        elif i=="W":
            D=west(D)
        elif i=="S":
            D=south(D)
        elif i=="L":
            D=left(D)
        else:
            D=right(D)
    return D
def same(c1,c2):
    for i in T:
        for j in U:
            D=change(i+j)
            flag=0
            for x in range(6):
                for y in range(6):
                    if d[x]==D[y]:
                        if c1[x]!=c2[y]:
                            flag=1
            if flag==0:
                return True
    return False
N=int(input())
c=[[int(i) for i in input().split()] for j in range(N)]
for i in range(N):
    for j in range(N):
        if i<j:
            if same(c[i],c[j]):
                print("No")
                exit()
print("Yes")

