import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

def main():
	h,w,k=MI()
	G=[]
	for i in range(h):
		A=list(map(int,input().rstrip().decode()))
		G.append(A)
	#print(G)

	for i in range(h):
		for j in range(w):
			if i!=0:
				G[i][j]+=G[i-1][j]
			if j!=0:
				G[i][j]+=G[i][j-1]
			if i!=0 and j!=0:
				G[i][j]-=G[i-1][j-1]
	#print(G)

	B=[]
	for i in range(2**(h-1)):
		C=[0,h-1]
		for j in range(h):
			if i&(1<<j):
				C.append(j)
				C.append(j+1)
		C.sort()
		B.append(C)

	#print(B)

	ans=10**10

	def check(x1,y1,x2,y2):
		ret=G[x2][y2]
		if x1 != 0:
			ret -= G[x1-1][y2]
		if y1 != 0:
			ret -= G[x2][y1-1]
		if x1 != 0 and y1 != 0:
			ret += G[x1-1][y1-1]
		return ret

	for D in B:
		#print(d)
		cnt=len(D)//2-1
		l=0
		ww=0
		f=0
		while ww<w and f==0:
			for i,j in zip(D[0::2],D[1::2]):
				#print(i,j)
				if check(i,l,j,ww)>k:
					#print(i,l,j,ww,check(i,l,j,ww))
					if l==ww:
						f=1
					else:
						cnt+=1
						l=ww
					break
			ww+=1
			#print(w,ww,cnt)
		#print(D,cnt)
		if f==0:
			ans=min(ans,cnt)
	print(ans)














if __name__ == "__main__":
	main()