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
	n,k=MI()
	mod=10**9+7

	f=[1]
	for i in range(1,n+10):
		f.append((f[-1]*i)%mod)
	finv=[]
	for i in f:
		finv.append(pow(i,mod-2,mod))

	ans=0
	for i in range(k+1):
		if n-i-1>=0:
			ans+=f[n]*finv[i]*finv[n-i]*f[n-1]*finv[i]*finv[n-i-1]
			ans%=mod
		else:
			break
	print(ans%mod)








if __name__ == "__main__":
	main()
