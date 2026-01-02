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
	h,w=MI()

	S=["#"*(w+1)]
	for _ in range(h):
		S.append("#"+input().rstrip().decode())
	#print(S)

	G=[[10**10]*(w+1) for _ in range(h+1)]

	if S[1][1]=="#":
		G[1][1]=1
	else:
		G[1][1]=0

	for i in range(1,h+1):
		for j in range(1,w+1):
			#print(G)
			if i==j==1:
				continue
			a=G[i-1][j]+(S[i-1][j]=="." and S[i][j]=="#")
			b=G[i][j-1]+(S[i][j-1]=="." and S[i][j]=="#")
			#print(i,j,a,b)
			G[i][j]=min(a,b)

	print(G[h][w])













if __name__ == "__main__":
	main()
