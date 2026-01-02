import sys
input = sys.stdin.readline
class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
 
    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]
 
    def same(self,x,y):
        return self.find(x) == self.find(y)
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.uf[x] > self.uf[y]:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]
def main():
    n,q = map(int,input().split())
    U = Unionfind(n)
    for i in range(q):
        t,u,v = map(int,input().split())
        if t == 0:
            U.union(u,v)
        else:
            print(int(U.same(u,v)))

if __name__ == "__main__":
    main()