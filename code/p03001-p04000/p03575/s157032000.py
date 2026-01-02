def root(nodes,x):
    if nodes[x] < 0:
        return x
    else:
        nodes[x] = root(nodes,nodes[x])
        return nodes[x]

def unite(nodes,x,y):
    root_x, root_y = root(nodes,x) , root(nodes,y)
    if root_x != root_y:
        nodes[root_x] = root_y

def is_same(nodes,x,y):
    return root(nodes,x) == root(nodes,y)


N,M = list(map(int,input().split()))
data = [[0 for s in range(2)] for k in range(M)]
for i in range(M):
    temp = input().split()
    data[i][0] = int(temp[0])-1
    data[i][1] = int(temp[1])-1
    
sum = 0

for i in range(M):
    nodes = [-1]*(N)
    for j in range(M):
        if j != i:
            unite(nodes,data[j][0],data[j][1])
    for k in range(1,N):
        if is_same(nodes,k-1,k):
            continue
        else:
            sum += 1
            break

print(sum)