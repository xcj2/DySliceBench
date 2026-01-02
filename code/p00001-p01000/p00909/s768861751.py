
import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

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
            return 10000000000

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
    
    def same(self,x,y):
        return self.find(x) == self.find(y)
        
    def size(self,x):
        return -self.parents[self.find(x)]

def solve(N,M):
    uf = WeightedUnionFind(N)
    for _ in range(M):
        q = input().split()
        if q[0] == '!':
            a,b,w = map(int,q[1:])
            a -= 1
            b -= 1
            uf.unite(a,b,w)
        else:
            a,b = map(int,q[1:])
            a -= 1
            b -= 1
            ans = uf.diff(a,b)
            if ans == 10000000000:
                print('UNKNOWN')
            else:
                print(ans)

def main():
    while True:
        N,M = map(int,input().split())
        if N == 0 and M == 0:
            break
        solve(N,M)
if __name__ == '__main__':
    main()
