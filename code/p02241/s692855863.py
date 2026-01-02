n = int(input())
T = [i for i in range(n)]
def root(x):
    path_to_root = []
    while T[x] != x:
        path_to_root.append(x)
        x = T[x]
    for node in path_to_root:
        T[node] = x
    return x
def is_same_set(x,y):
    return root(x) == root(y)
def unite(x,y):
    T[root(x)] = root(y)

A = []
W = []
for i in range(n):
    A.append(list(map(int,input().strip().split(' '))))
    for j in range(i+1,n):
        if A[i][j] != -1:
            W.append([A[i][j],i,j])
W.sort()
sum = 0
for i in range(len(W)):
    if not is_same_set(W[i][1],W[i][2]):
        unite(W[i][1],W[i][2])
        sum += W[i][0]
print(sum)

