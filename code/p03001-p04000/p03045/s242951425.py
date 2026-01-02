n,m=map(int,input().split())
a=[]
for i in range(m):
    x,y,z=map(int,input().split())
    a.append((x-1,y-1))

class union:
    def __init__(self,num):
        self.par=[-1]*num
    def get_par(self,node):
        if self.par[node]==-1:
            return node
        else:
            x=self.get_par(self.par[node])
            return x
    def merge(self,x,y):
        X=self.get_par(x)
        Y=self.get_par(y)
        if X!=Y:
            self.par[Y]=X
    def output(self):
        print(self.par)
    def count(self):
        print(self.par.count(-1))
def get_parent(node):
    if par[node]==-1:
        return node
    else:
        par[node]=get_parent(par[node])
        return par[node]
    
def merge(x,y):
    i=get_parent(x)
    j=get_parent(y)
    if i!=j:
        par[i]=j
    return
par=[-1]*n
for i in range(m):
    merge(a[i][0],a[i][1])
print(par.count(-1))