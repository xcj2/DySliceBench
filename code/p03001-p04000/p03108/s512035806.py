class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):

        x = self.Find_Root(x)
        y = self.Find_Root(y)

        if(x == y):
            return 

        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y

            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]

def main():
    n,m = map(int,input().split())
    ls = [[int(x) for x in input().split()] for _ in range(m)]
    ans = [0 for _ in range(m+1)]
    ans[m] = n*(n-1)//2
    union = UnionFind(n)
    for i in reversed(range(m)):
        a,b = ls[i]
        if ans[i+1]==0:
            pass
        else:
            if union.isSameGroup(a,b):
                ans[i] = ans[i+1]
            else:
                ans[i] = max(0,ans[i+1] - union.Count(a)*union.Count(b))
                union.Unite(a,b)

    for i in range(1,m+1):
        print(ans[i])



if __name__ == "__main__":
    main()