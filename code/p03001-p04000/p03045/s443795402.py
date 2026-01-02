N,M=map(int,input().split())
XYZ=[]
for i in range(M):
    X,Y,Z=map(int,input().split())
    XYZ.append([X,Y])

def find_root(root,x):
    y = root[x]
    if x == y:
        return x
    z = find_root(root,y)
    root[x] = z
    return z
 
def merge(root,size,x,y):
    x = find_root(root,x)
    y = find_root(root,y)
    if x == y:
        return
    sx,sy = size[x],size[y]
    if sx < sy:
        sx,sy = sy,sx
        x,y = y,x
    root[y] = x
    size[x] += sy
    
def UF_make(graph,n):
    Root=list(range(n+1))
    Size=[1] * (n+1)
    for i in range(len(graph)):
        merge(Root,Size,graph[i][0],graph[i][1])
    for i in range(n+1):
        Root[i] = find_root(Root,i)
    Root.pop(0)
    return Root

L=UF_make(XYZ,N)
print(len(set(L)))