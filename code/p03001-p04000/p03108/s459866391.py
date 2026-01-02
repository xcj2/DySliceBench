n,m = map(int,input().split())


def comb(x,y):
    r = 1
    for i in range(x,x-y,-1):
        r *= i
    for i in range(y,0,-1):
        r //= i
    return r
def find(ID,a):
    tmp = a
    while tmp !=ID[tmp]:
        tmp = ID[tmp]
    return tmp
def union(ID,a,b):
    ida = find(ID,a)
    idb = find(ID,b)
    if ida!=idb:
        ID[a] = idb
        ID[b] = idb
        ID[ida] = idb
        tmp = SIZE[idb]*SIZE[ida]
        SIZE[idb] += SIZE[ida]
        return tmp 
    return 0
bridges = []
res = []
ID = []
SIZE = []
cnt = comb(n,2)
for i in range(n+1):
    ID.append(i)
    SIZE.append(1)
for i in range(m):
    a,b = map(int,input().split())
    bridges.append((a,b))

for i in range(m-1,-1,-1):
    res.append(cnt)
    cnt -= union(ID,bridges[i][0],bridges[i][1])
    

for i in range(m-1,-1,-1):
    print(res[i])            
