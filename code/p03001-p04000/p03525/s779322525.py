import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

def main():
	n=II()
	D=LI()+[0]

	D.sort()
	#print(D)

	DD=[]

	for i,v in enumerate(D):
		if i%2==0:
			DD.append(v)
		else:
			DD.append(24-v)
	DD.sort()
	DD.append(24)

	#print(DD)

	ans=25

	for i,j in zip(DD[:-1],DD[1:]):
		ans=min(ans,j-i)
	print(ans)











if __name__ == "__main__":
	main()
