MAX = 1000001

class Query:
    def __init__(self, l, r, idx): 
        self.l = l 
        self.r = r 
        self.idx = idx 
  
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
  
def answeringQueries(arr, n, queries, q): 
  
    # initialising bit array 
    bit = BIT(n)
  
    # holds the rightmost index of  
    # any number as numbers of a[i] 
    # are less than or equal to 10^6 
    last_visit = [-1] * MAX
  
    # answer for each query 
    ans = [0] * q 
  
    query_counter = 0
    for i in range(n): 
  
        # If last visit is not -1 update -1 at the 
        # idx equal to last_visit[arr[i]] 
        if last_visit[arr[i]] != -1: 
            bit.update(last_visit[arr[i]] + 1, -1)
  
        # Setting last_visit[arr[i]] as i and  
        # updating the bit array accordingly 
        last_visit[arr[i]] = i 
        bit.update(i + 1, 1)
  
        # If i is equal to r of any query store answer 
        # for that query in ans[] 
        while query_counter < q and queries[query_counter].r == i: 
            ans[queries[query_counter].idx] = bit.sum(queries[query_counter].r + 1) -bit.sum(queries[query_counter].l)
            query_counter += 1
  
    # print answer for each query 
    for i in range(q): 
        print(ans[i]) 
  
# Driver Code 
if __name__ == "__main__": 
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    # n = len(a)
    queries = []
    for i in range(q):
        l,r = map(int,input().split())
        queries.append(Query(l-1,r-1,i))
    # queries = [Query(0, 4, 0),
    #            Query(1, 3, 1),
    #            Query(2, 4, 2)]
    # q = len(queries)
  
    queries.sort(key = lambda x: x.r) 
    answeringQueries(a, n, queries, q)
