c=[int(i) for i in input().split()]
S=input()
d=[(0,0,1),(-1,0,0),(0,1,0),(0,-1,0),(1,0,0),(0,0,-1)]
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
D=[i for i in d]
for i in S:
    if i=="N":
        D=north(D)
    elif i=="S":
        D=south(D)
    elif i=="W":
        D=west(D)
    else:
        D=east(D)
for k in range(6):
    if D[k]==(0,0,1):
        print(c[k])

