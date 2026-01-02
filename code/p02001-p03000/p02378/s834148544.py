def outer(x,match,phi):
    if(match[x]==x or phi[match[x]]!=match[x]):
        return True
    return False
    
def inner(x,match,phi):
    if(match[x]!=x and phi[match[x]]==match[x] and phi[x]!=x):
        return True
    return False

def F(x,match,phi):
    if(match[x]!=x and phi[match[x]]==match[x] and phi[x]==x):
        return True
    return False
       
def disjoint(x,y,V,phi,match):
    usedx=[False]*V
    prex=match[x]
    while not (usedx[x] and usedx[prex]) :
        usedx[prex]=True
        usedx[x]=True
        x=phi[prex]
        prex=match[x]
    usedy=[False]*V
    prey=match[y]
    while not (usedy[y] and usedy[prey]) :
        usedy[y]=True
        usedy[prey]=True
        if usedx[y] or usedx[prey]:
            return False
        prey=match[y]
        y=phi[prey]
    return True
    
def shrink(x,y,match,rho,phi,V):
    r=firstvertex(x,y,match,phi,rho,V)
    v=match[x]    
    if x!=r and x!=v:
        while True:
            if rho[phi[v]]!=r:
                phi[phi[v]]=v
            if(phi[v]==r or match[phi[v]]==r):
                break
            v=match[phi[v]]
    v=match[y]
    if y!=r and y!=v:
        while True:
            if rho[phi[v]]!=r:
                phi[phi[v]]=v
            if(phi[v]==r or match[phi[v]]==r):
                break
            v=match[phi[v]]
#             print(y,v,phi[v],r)
    if rho[x]!=r:
        phi[x]=y
    if rho[y]!=r:
        phi[y]=x
        
    used=[False]*V
    used[r]=True
    while x!=r or y!=r: 
        used[x]=True
        used[y]=True
        if(x!=r):
            x=match[x]
        if y!=r:
            y=match[y]
        used[x]=True
        used[y]=True
        if x!=r:
            x=phi[x]
        if y!=r:
            y=phi[y]
    for i in range(V):
        if used[rho[i]] :
            rho[i]=r
    
def firstvertex(x,y,match,phi,rho,V):
    usedx=[False]*V
    usedy=[False]*V
    flag=True
    while True:
        if usedy[x] and rho[x]==x:
            return x
        usedx[x]=True
        if usedx[y] and rho[y]==y:
            return y
        usedy[y]=True
        if flag:
            x=match[x]
            y=match[y]
            flag=False
        else:
            x=phi[x]
            y=phi[y]
            flag=True
       
def augment(x,y,match,phi,V):
    v=match[x]
    used=[False]*V
    used[x]=True
    while not used[v]:
        used[v]=True
        used[phi[v]]=True
        tmp=match[phi[v]]
        match[phi[v]]=v
        match[v]=phi[v]
        v=tmp
    v=match[y]
    used=[False]*V
    used[y]=True
    while not used[v]:
        used[v]=True
        used[phi[v]]=True
        tmp=match[phi[v]]
        match[phi[v]]=v
        match[v]=phi[v]
        v=tmp
    match[x]=y
    match[y]=x
    
    
def Edmonds(graph,V):
    match=[i for i in range(V)]
    phi=[i for i in range(V)]
    rho=[i for i in range(V)]
    scanned=[False]*V
    
    while True:
#         from IPython.core.debugger import Pdb; Pdb().set_trace()
        flag=True
        for i in range(V):
            if (not scanned[i]) and outer(i,match,phi):
                x=i
                flag=False
                break
        if flag:
            break
        for y in graph[x]:
            if F(y,match,phi):
                #拡大
                phi[y]=x
                continue
            if not(outer(y,match,phi) and rho[y]!=rho[x]):
                continue
                
            if disjoint(x,y,V,phi,match):
                #増加
                augment(x,y,match,phi,V)
                scanned=[False]*V
                rho=[i for i in range(V)]
                phi=[i for i in range(V)]
                flag=True
                break
            #縮小
            shrink(x,y,match,rho,phi,V)
        if not flag:
            scanned[x]=True
    cnt=0
    for i in range(V):
        if match[i]!=i:
            cnt+=1
#     print(match)
    return int(cnt/2)
        




x,y,e=list(map(int,input().split()))
v=x+y
graph=[[]for _ in range(v)]

for i in range(e):
    tmp1,tmp2=list(map(int,input().split()))
    tmp2+=x
    graph[tmp1].append(tmp2)
    graph[tmp2].append(tmp1)

cnt=Edmonds(graph,v)
print(cnt)


    
