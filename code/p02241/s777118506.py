def root(x):
    path = []
    while P[x] != x:
        path.append(x)
        x = P[x]
    for node in path:
        P[node] = x
    return x
def check(x,y):
    if root(x) == root(y):
        return 1
    else:
        return 0
def unite(x,y):
    P[root(x)] = root(y)        

n = int(input())
P = [i for i in range(n)]
omomi = []
for k in range(n):
    s = list(map(int,input().split()))
    for l in range(n):
        if s[l] != -1:
            omomi.append([s[l],k,l])
omomi.sort()
ans = 0
for yee in range(len(omomi)):
    if check(omomi[yee][1],omomi[yee][2]) == False:
            unite(omomi[yee][1],omomi[yee][2])
            ans+=omomi[yee][0]
print(ans)            
