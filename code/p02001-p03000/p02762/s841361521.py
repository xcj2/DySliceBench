class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



def main():
    n,m,k = map(int,input().split())
    friend = [[] for i in range(n)]
    block = [[] for i in range(n)]

    for i in range(m):
        a,b = map(lambda x: int(x)-1,input().split())
        friend[a].append(b)
        friend[b].append(a)
    # print(friend)
    
    for i in range(k):
        c,d = map(lambda x:int(x)-1,input().split())
        block[c].append(d)
        block[d].append(c)
    
    # print(block)

    un = UnionFind(n)
    
    for i in range(len(friend)):
        for j in range(len(friend[i])):
            # print(i,friend[i][j])
            un.union(i,friend[i][j])
    
    ans = []
    for i in range(len(block)):
        cnt = 0
        for j in range(len(block[i])):
            # print(i,block[i][j])
            if un.find(i) == un.find(block[i][j]):
                cnt += 1
        ans.append(str(un.size(i)-len(friend[i]) - cnt - 1))

    # for i in range(n):
    #     # ans.append(str(len((set(un.members(i)) - (set(block[i])|set(friend[i]))))-1))
    #     print(un.size(i))
    #     print(len(friend[i]))
    #     print(len(block[i]))
    #     ans.append(str( un.size(i) - len(friend[i]) - len(block[i]) -1))

    print(' '.join(ans))

    return


if __name__ == "__main__":
    main()


