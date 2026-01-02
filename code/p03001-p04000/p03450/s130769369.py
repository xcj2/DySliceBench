MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

class WeightedUnionFind():

    def __init__(self,N):
        self.N = N
        self.parents = [-1] * self.N
        self.diff_weight = [0] * self.N
    
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            p = self.find(self.parents[x])
            self.diff_weight[x] += self.diff_weight[self.parents[x]]
            self.parents[x] = p
            return p
    
    def weight(self,x):#xの親からの重みを返す
        self.find(x)
        return self.diff_weight[x]
    
    def diff(self,x,y):#同じグループにいたらxとyの重みの差を返す
        if self.find(x) == self.find(y):
            return self.weight(y) - self.weight(x)
        else:
            return 1e10

    def unite(self,x,y,w):#wieght(y) = weight(x) + dとなるように合体
        w += self.weight(x)
        w -= self.weight(y)

        x = self.find(x)
        y = self.find(y)
        if x == y:
            if self.diff(x,y) == w:
                return True
            else:
                return False

        if self.parents[x] > self.parents[y]:
            x,y = y,x
            w *= -1
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.diff_weight[y] = w
        return True
    
    def size(self,x):
        return - self.parents[self.find(x)]

def main():
    n,m = map(int,input().split())
    uf = WeightedUnionFind(n)
    flag = True
    for _ in range(m):
        l,r,d = map(int,input().split())
        l -= 1
        r -= 1
        if uf.unite(l,r,d):
            continue
        else:
            flag = False
            break
    print('Yes' if flag else 'No')
if __name__ == '__main__':
    main()