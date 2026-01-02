def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b


h,w = getMN()
pos = ["."]*(w*h+5000)
cur = 1

class unionfind():
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        self.childnum = [1] * (n + 1)
        self.childb = [0 if pos[i] == "." else 1 for i in range(n+1)]

    def find(self,x):
        if self.par[x] == x:
            return x
        else:
            #print(x, ":", self.par[x])
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.childnum[y] += self.childnum[x]
            self.childb[y] += self.childb[x]

        else:
            self.par[y] = x
            self.childnum[x] += self.childnum[y]
            self.childb[x] += self.childb[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same_check(self,x,y):
        return self.find(x) == self.find(y)


for i in range(h):
    posin = input()
    for j in range(w):
        if posin[j] == "#":
            pos[j+(i)*w] = "#"

uf = unionfind(h*w+1)

unionlog = []

for i in range(h):
    for j in range(w):
        nn = j+(i)*w
        now = pos[nn]

        if j != w-1:
            nr = j + (i) * w + 1
            right = pos[nr]
            if right != now:
                if not uf.same_check(nn,nr):
                    uf.union(nn,nr)
                    unionlog.append("union:{},{}".format(nn,nr))
        if i != h-1:
            nd = j + (i + 1) * w
            down = pos[nd]
            if down != now:
                if not uf.same_check(nn,nd):
                    uf.union(nn,nd)
                    unionlog.append("union:{},{}".format(nn,nd))


a = 0
#print("\n".join(unionlog))

#print("s",uf.childnum)
#print(uf.childb)
#print([uf.find(i) for i in range(9)])
ans = 0

for parnum in list(set([uf.find(i) for i in range(h*w)])):
    #print(parnum)
    b = uf.childb[parnum]
    w = uf.childnum[parnum] - b
    #print(b,w)
    ans +=  b*w

print(ans)