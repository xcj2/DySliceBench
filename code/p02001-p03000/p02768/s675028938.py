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
	m=10**9+7
	n,a,b=MI()
	f=[1]
	for i in range(b+5):
		t=f[-1]*(n-i)*pow(i+1,m-2,m)
		t%=m
		f.append(t)
	#print(f)

	ans=pow(2,n,m)-1-f[a]-f[b]
	ans%=m
	print(ans)




























if __name__ == "__main__":
	main()
