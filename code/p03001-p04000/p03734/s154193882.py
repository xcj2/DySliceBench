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
	n,ww=MI()
	w1,v1=MI()
	li=[[] for _ in range(4)]
	li[0].append(v1)

	for _ in range(n-1):
		w,v=MI()
		li[w-w1].append(v)

	for i in range(4):
		li[i]=[0]+sorted(li[i],reverse=True)
	#print(li)

	for i in range(4):
		for j in range(len(li[i])-1):
			li[i][j+1]+=li[i][j]
	#print(li)

	ans=0

	for i0 in range(len(li[0])):
		for i1 in range(len(li[1])):
			for i2 in range(len(li[2])):
				for i3 in range(len(li[3])):
					#print(i0,i1,i2,i3,li[0][i0],li[1][i1],li[2][i2],li[3][i3],w1*i0+(w1+1)*i1+(w1+2)*i2+(w1+3)*i3,li[0][i0]+li[1][i1]+li[2][i2]+li[3][i3],w,ans)
					if w1*i0+(w1+1)*i1+(w1+2)*i2+(w1+3)*i3<=ww:
						ans=max(ans,li[0][i0]+li[1][i1]+li[2][i2]+li[3][i3])

	print(ans)


if __name__ == "__main__":
	main()
