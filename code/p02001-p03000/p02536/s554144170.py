N,M = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(M)]

par = [0]*(N+1)

for i in range (N+1): #[0,1,2,...,N]を作成
    par[i] = i

#木の根を求める関数
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

#根が同じならTrue,別ならFalseを返す関数
def find(x,y):
    return root(x)==root(y)

#経路を圧縮して連結させる関数
def union(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    par[x] = y

for l in L:
    union(l[0],l[1])

R = [0]
R[0] = root(par[1])
for i in range(2,N+1):
    if R[0] != root(par[i]):
        R.append(root(par[i]))

print(len(set(R))-1)