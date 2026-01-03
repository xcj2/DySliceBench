import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
#input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

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
	n=II()
	X=[]
	Y=[]
	for i in range(n):
		x,y=MI()
		X.append((x,i))
		Y.append((y,i))
	X.sort()
	Y.sort()
	#print(X,Y)

	li=[]
	for i in range(n-1):
		li.append((X[i+1][0]-X[i][0],X[i+1][1],X[i][1]))
		li.append((Y[i+1][0]-Y[i][0],Y[i+1][1],Y[i][1]))
	li.sort()
	#rint(li)

	UF=UnionFind(n)
	k=0
	ans=0
	for d,s,t in li:
		if k==n-1:
			break
		if UF.same(s,t):
			continue
		else:
			ans+=d
			UF.union(s,t)
			k+=1
	print(ans)

if __name__ == "__main__":
	main()