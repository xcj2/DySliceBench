import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()


def main():
	d,g=MI()
	P=[]
	C=[]
	for _ in range(d):
		p,c=MI()
		P.append(p)
		C.append(c)
	#print(P,C)

	ans=10**10

	for i in range(1<<d):
		cnt=0
		gg=0
		for j in range(d):
			if i&1<<j:
				cnt+=P[j]
				gg+=P[j]*100*(j+1)+C[j]
		#print(i,cnt,gg)

		for j in reversed(range(d)):
			if not i&1<<j:
				if gg+(P[j]-1)*100*(j+1)>=g:
					cnt+=max(0,-((-g+gg)//(100*(j+1))))
					gg=g
					break
				else:
					cnt+=P[j]-1
					gg+=(P[j]-1)*100*(j+1)

		if gg>=g:
			ans=min(ans,cnt)
	print(ans)

















if __name__ == "__main__":
	main()
