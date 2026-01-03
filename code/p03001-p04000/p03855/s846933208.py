N,K,L=map(int,input().split())
PQ=[list(map(int,input().split())) for i in range(K)]
RS=[list(map(int,input().split())) for i in range(L)]

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
    Root.pop(0)  #
    return Root

PQN=UF_make(PQ,N)
RSN=UF_make(RS,N)
PQRS=[PQN[i]*10**6+RSN[i] for i in range(N)]
D=len(set(PQRS))
PQRS=[[PQRS[i],i,0] for i in range(N)]
PQRS.sort()

p=0
while p<N:
    i=1
    c=0
    if p+i>N-1:
        break
    while PQRS[p][0]==PQRS[p+i][0]:
        c+=1
        i+=1
        if p+i>N-1:
            break
    for j in range(p,p+i):
        PQRS[j][2]=c
    p+=i
PQRS.sort(key=lambda x:x[1])
for i in range(N):
    print(PQRS[i][2]+1,end=' ')