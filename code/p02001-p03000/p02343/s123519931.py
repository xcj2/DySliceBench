p=[]
rank=[]
answer=[]

def makeset(x):
    p[x] = x
    rank[x] = 0
    
def union(x,y):
    link(findset(x),findset(y))
    
def link(x,y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y] + 1
def findset(x):
    if x != p[x]:
        p[x] = findset(p[x])
    return p[x]

t,s = map(int,input().split())
for i in range(t):
    p.append(None)
    rank.append(None)
while True:
    try:
        o,x,y = map(int,input().split())
    except:
        break
    else:
        if o == 0:
            if p[x] == None:
                makeset(x)
            if p[y] == None:
                makeset(y)
            union(x,y)
        else:
            if p[x] == None:
                makeset(x)
            if p[y] == None:
                makeset(y)
            if findset(x) == findset(y):
                answer.append(1)
            else:
                answer.append(0)
for i in range(len(answer)):
    print(answer[i])        
