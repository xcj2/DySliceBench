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
	n,m,k=MI()
	mod=998244353
	
	f=[1]
	for i in range(1,n+10):
		f.append((f[-1]*i)%mod)
	finv=[]
	for i in f:
		finv.append(pow(i,mod-2,mod))
	
	mp=[1]
	for i in range(1,n+10):
		mp.append((mp[-1]*(m-1))%mod)
		
	
	ans=0
	for kk in range(k+1):
		cnt=f[n-1]*finv[kk]*finv[n-1-kk]
		cnt%mod
		cnt*=m*mp[n-kk-1]
		ans+=cnt
		ans%mod
	print(ans%mod)













if __name__=="__main__":
	main()
