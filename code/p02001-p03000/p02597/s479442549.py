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
	s=input().rstrip().decode()

	w=[0]*(n+1)
	r=[0]*(n+1)

	for i,ss in enumerate(s):
		if ss=="W":
			w[i+1]=w[i]+1
		else:
			w[i+1]=w[i]

	for i,ss in enumerate(reversed(s)):
		if ss=="R":
			r[i+1]=r[i]+1
		else:
			r[i+1]=r[i]

	#print(w,r)

	ans=0
	for i,j in zip(w[1:],reversed(r[1:])):
		ans=max(ans,min(i,j))
	print(ans)




if __name__ == "__main__":
	main()
