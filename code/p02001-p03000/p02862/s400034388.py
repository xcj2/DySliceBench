import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

#1400

def main():
	x,y=MI()
	mod=10**9+7

	a=2*y-x
	b=2*x-y

	if a%3!=0 or b%3!=0 or a<0 or b<0:
		print(0)
		exit(0)

	a//=3
	b//=3

	f=[1]
	for i in range(1,10**6):
		f.append(f[-1]*i%mod)

	ans=f[a+b]*pow(f[a],mod-2,mod)*pow(f[b],mod-2,mod)
	print(ans%mod)


if __name__ == "__main__":
	main()