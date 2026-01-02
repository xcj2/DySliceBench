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
	r1,c1,r2,c2=MI()
	m=10**9+7

	ff=[1]

	for i in range(1,2*10**6+5):
		ff.append(ff[-1]*i%m)


	def f(r,c):
		return (ff[r+c]*pow(ff[r],m-2,m)*pow(ff[c],m-2,m))%m

	ans=0
	ans+=f(r2+1,c2+1)
	ans+=f(r1,c1)
	ans-=f(r2+1,c1)
	ans-=f(r1,c2+1)

	print(ans%m)



if __name__ == "__main__":
	main()
