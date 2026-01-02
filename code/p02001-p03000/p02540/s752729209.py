import sys
from collections import deque
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1]*(n+1)#それぞれの要素がどの要素の子であるか

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]#それぞれの要素の根を再帰的に求める

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)#x,yが同じ集合に属するかどうか
    
    def size(self, x):
        return -self.par[self.find(x)]
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if root == self.find(i)]        


def main():
    n = int(input())
    town = [list(map(int, input().split())) + [i] for i in range(n)]

    town.sort()
    union = UnionFind(n)
    already = deque([])

    for x, y, i in town:
        if not already:
            already.append((y, i))
            continue
        key = already.pop()
        if key[0] > y:
            already.append(key)
            already.append((y, i))
            continue
        sub = key
        while already:
            union.union(sub[1], i)
            sub = already.pop()
            if sub[0] > y:
                break
        if not already and sub[0] < y:
            union.union(sub[1], i)
        else:
            already.append(sub)
        already.append(key)
    
    ans = [0]*n
    for i in range(n):
        ans[i] = union.size(i)
    
    print(*ans, sep="\n")





    
if __name__ == "__main__":
    main()

