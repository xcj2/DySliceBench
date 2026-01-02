ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))
lis = lambda x : int(x.replace('.',''))
li2 = lambda : list(map(lis,input().split()))

# かぶっているか判定
# 最短判定

import math

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.d = [-1] * n

    def find(self, x):
        if(self.d[x] < 0):
            return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return False
        if(self.d[x] > self.d[y]):
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self,x):
        return -self.d[self.find(x)]

def judgeContact(a,b):
    # k = (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 - (a[3] + b[3]) ** 2
    k = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) - (a[3] + b[3]) 
    if k <= 0:
        return -1
    else:
        return k

def calc(n):
    ps = []
    uf = UnionFind(n)
    d = []
    cnt = 0
    ans = 0

    for i in range(n):
        p = li2()
        
        # かぶり判定
        for k,j in enumerate(ps):
            v = judgeContact(p,j) 
            if v == -1:
                # d.append([0,i,k])
                if uf.same(i,k) == False:
                    uf.union(i,k)
                    cnt += 1
            else:
                d.append([v,i,k])
        ps.append(p)

    d.sort()
    for i in d:
        if cnt == n-1:
            break

        if uf.same(i[1],i[2]):
            continue
        
        uf.union(i[1],i[2])
        # print('union',i[1],i[2],cnt,i[0])
        cnt += 1
        ans += i[0]

    
    print("{:.3f}".format(ans/1000))


while 1:
    n = ii()
    if n == 0:
        break
    
    calc(n)
