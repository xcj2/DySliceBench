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
# rstrip().decode()


def main():
	n=II()

	pf={}
	for i in range(2,int(n**0.5)+1):
		while n%i==0:
			pf[i]=pf.get(i,0)+1
			n//=i
	if n>1:pf[n]=1
	#print(pf)

	li={}
	for k in pf:
		li[pf[k]]=li.get(pf[k],0)+1
	#print(li)

	p=[]
	for i in range(10):
		p+=[i]*(i+1)
	#print(p)

	ans=0
	for i in li:
		ans+=li[i]*p[i]
	print(ans)







if __name__ == "__main__":
	main()
