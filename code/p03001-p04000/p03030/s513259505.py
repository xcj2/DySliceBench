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
	A=[]
	for i in range(1,n+1):
		a,b=input().split()
		a=a.rstrip().decode()
		b=int(b)
		A.append([a,b,i])

	A.sort(key=lambda x:x[1],reverse=True)
	A.sort(key=lambda x:x[0])

	for _,_,i in A:
		print(i)






if __name__ == "__main__":
	main()
