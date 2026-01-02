import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class Seg_sum():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 0
        self.func = lambda a,b : a+b

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res

n = int(readline())
xy = [ list(map(int,i.split()))  for i in readlines()]
mod = 998244353

xy.sort()
ys = [i[1] for i in xy]
ys.sort()
y_rank = {}
for i,y in enumerate(ys):
    y_rank[y] = i


point = [[0,0] for _ in range(n)]
for i,(x,y) in enumerate(xy):
    point[i][0] = i
    point[i][1] = y_rank[y]

seg = Seg_sum([0] * (n+10))

cnt = [[0,0,0,0] for _ in range(n)]
for x,y in point:
    cnt[x][2] = seg.query(0,y)
    cnt[x][1] = seg.query(y,n)
    cnt[x][0] = n-y-1 - cnt[x][1]
    cnt[x][3] = y - cnt[x][2]
    seg.update(y,1)

ex2 = [1] * (n)
for i in range(1,n):
    ex2[i] = (ex2[i-1]*2)%mod

ans = (ex2[n-1] * n) % mod
for n1,n2,n3,n4 in cnt:
    ans += (ex2[n1]-1)*(ex2[n3]-1)*ex2[n2+n4]
    ans %= mod
    ans += (ex2[n2]-1)*(ex2[n4]-1)*ex2[n1+n3]
    ans %= mod
    ans -= (ex2[n1]-1)*(ex2[n2]-1)*(ex2[n3]-1)*(ex2[n4]-1)
    ans %= mod

print(ans)