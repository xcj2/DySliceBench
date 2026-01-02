def root(x):
    path_to_root = []
    while P[x] != x:
        path_to_root.append(x)
        x = P[x]
    for node in path_to_root:
        P[node] = x
    return x
def is_same_set(x,y):
    return root(x) == root(y)
def unite(x,y):
    P[root(x)] = root(y)
    
    

n= int(input())
a=[]
P=[i for i in range(n)]

for i in range(n):
    temp= list(map(int,input().split()))
    for j in range(i,n):
        if temp[j] != -1:
            a.append([temp[j], i, j])
a.sort()
ans=0
for i in a:
    if not(is_same_set(P[i[1]],P[i[2]])):
        unite(i[1],i[2])
        ans+= i[0]
print(ans)
