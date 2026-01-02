#UnionFind
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
p = list(map(int,input().split()))
x_y = [list(map(int,input().split())) for i in range(M)]
nodes = [-1]*(N+1)
cnt = 0

for x,y in x_y:
    unite(nodes,x,y)


for i in range(N):
    if is_same(nodes,i+1,p[i]):cnt += 1

print(cnt)