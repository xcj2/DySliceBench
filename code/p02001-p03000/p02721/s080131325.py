import sys

input=sys.stdin.buffer.readline


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
def main():
	n,k,c=MI()
	s=input().rstrip().decode()
	
	kk=k
	i=0
	L=[]
	while kk:
		if s[i]=="o":
			L.append(i+1)
			i+=c+1
			kk-=1
		else:
			i+=1
		
	kk=k
	i=n-1
	R=[]
	while kk:
		if s[i]=="o":
			R.append(i+1)
			i-=c+1
			kk-=1
		else:
			i-=1
	R.sort()
	
	for i,j in zip(L,R):
		if i==j:
			print(i)
	
	
	
	
	
	
	
	

if __name__=="__main__":
	main()
