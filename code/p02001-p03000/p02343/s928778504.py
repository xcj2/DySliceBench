rank = {}
p = {}
        
def makeSet(x):
    p[x] = x
    rank[x] = 0

def link(x, y):
    if  rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if  rank[x] == rank[y]:
        rank[y] += 1

def union(x, y):
    link(findSet(x), findSet(y))
    
def findSet(x):
    if  x != p[x]:
        p[x] = findSet(p[x])
    return p[x]
    
def isSameSet(x, y):
    return findSet(x) == findSet(y)

n, q = map(int, input().split())
for x in range(n):
    makeSet(x)

for i in range(q):
    a,x,y = map(int, input().split())
    ret = (union if a == 0 else isSameSet)(x,y)
    if ret is None: continue
    if ret == True: print(1)
    else: print(0)