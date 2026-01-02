import sys
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
	G=[]
	for _ in range(n):
		s=input().rstrip().decode()
		G.append(list(s*2))

	ans=0
	for x in range(n):
		f=1
		for i in range(n):
			if f==0:
				break
			for j in range(n):
				#print(i,j)
				if G[i][j]!=G[j-x][i+x]:
					f=0
					break
		else:
			#print(x)
			ans+=n
	print(ans)










if __name__ == "__main__":
	main()
