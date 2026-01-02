import sys
#input = sys.stdin.buffer.readline

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

class BinaryIndexedTree:
	def __init__(self,n,default=0):
		self.s=[default]*(n+1)
		self.n=n
	
	def add(self,val,idx):
		while idx<self.n+1:
			self.s[idx]=self.s[idx]+val
			idx+=idx&(-idx)
		return
	
	def get(self,idx):
		res=0
		while idx>0:
			res=res+self.s[idx]
			idx-=idx&(-idx)
		return res

from collections import defaultdict

def main():
	n=II()
	s=input()
	S=[0]+list(s)
	
	d=defaultdict(lambda:BinaryIndexedTree(n))
	
	for i,si in enumerate(s):
		#print(i,si)
		d[si].add(1,i+1)
	
	q=II()
	for _ in range(q):
		f,a,b=input().split()
		if int(f)==1:
			a=int(a)
			d[S[a]].add(-1,a)
			d[b].add(1,a)
			S[a]=b
		else:
			#print(S,a,b)
			a=int(a)
			b=int(b)
			cnt=0
			for bit in d.values():
				if bit.get(b)-bit.get(a-1)>0:
					cnt+=1
			print(cnt)
		
	

if __name__=="__main__":
	main()
