import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

#2320
#import numpy as np

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
	n,m=MI()
	e=[]
	for _ in range(m):
		a,b=MI()
		a-=1
		b-=1
		e.append([a,b])
	#print(e)

	UF=UnionFind(n)
	ans=[]
	tmp=n*(n-1)//2

	for li in reversed(e):
		ans.append(tmp)
		a=li[0]
		b=li[1]
		if UF.same(a,b):
			continue
		aa=UF.parents[UF.find(a)]
		bb=UF.parents[UF.find(b)]
		#print(a,b,aa,bb)
		tmp-=aa*bb
		UF.union(a,b)
	print("\n".join(str(i) for i in ans[::-1]))




if __name__ == "__main__":
	main()