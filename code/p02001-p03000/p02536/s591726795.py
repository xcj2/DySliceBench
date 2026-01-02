# n,m=map(int,input().split())
# a=[]
# a.append(list(map(int,input().split())))

n,m, = map(int,input().split())
par = [i for i in range(n+1)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

def size(x):
    return -par[find(x)]

# def size(self, x):
#         return -self.parents[self.find(x)]

for i in range(m):
    a,b = map(int,input().split())
    unite(a,b)

li = [0]*(n+1)
for i in range(1,n+1):
    li[(-size(par[i]))] = 1

print(li.count(1)-1)