class BIT:
    def __init__(self,n):
        self.n = n
        self.tree = [0]*(n+1)

    def sum(self,x):
        sum = 0
        while(x>0):
            sum+=self.tree[x]
            x-=x&(-x)
        return sum

    def update(self,x,k):
        while(x<=self.n):
            self.tree[x]+=k
            x+=x&(-x)

    def build(self,a):
        for i in range(len(a)):
            k = a[i]
            x = i+1
            while(x<=self.n):
                self.tree[x]+=k
                x+=x&(-x)
class Query:
    def __init__(self, r,l, idx):
        self.l = l
        self.r = r
        self.idx = idx

def solve(case):
    n,q = map(int,input().split())
    c = list(map(int,input().split()))
    query = []
    for i in range(q):
        l,r = map(int,input().split())
        query.append(Query(r,l,i))

    query.sort(key = lambda x:x.r)
    bit = BIT(n)
    lastvis = [-1]*(n+1)
    ind = 0
    ans = [0]*q
    for i in range(n):
        if(lastvis[c[i]] != -1):
            bit.update(lastvis[c[i]]+1,-1)

        lastvis[c[i]] = i
        bit.update(i+1,1)
        while(ind<q and query[ind].r == i+1):
            ans[query[ind].idx] = (bit.sum(i+1) - bit.sum(query[ind].l-1))
            ind+=1

    # print('\n'.join(str(ans[i]) for i in range(len(ans))))
    for i in range(q):
        print(ans[i])
solve(1)
