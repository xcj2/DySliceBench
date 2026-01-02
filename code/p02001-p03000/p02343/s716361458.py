# class UnionFind:
#
#     def __init__(self,n):
#         self.roots = range(n)
#
#     def

def root(i):
    if par[i] == i:
        return i

    par[i]=root(par[i])
    return par[i]

def unite(x,y):
    xr = root(x)
    yr = root(y)
    par[yr] = xr

def same(x,y):
    return root(x)==root(y)



n,q = map(int,input().split())

par = list(range(n))

for i in range(q):
    commands = list(map(int,input().split()))
    if commands[0] == 0:
        unite(commands[1], commands[2])
    if commands[0] == 1:
        if same(commands[1], commands[2]):
            print(1)
        else:
            print(0)