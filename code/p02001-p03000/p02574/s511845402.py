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
	nn=II()
	A=LI()
	ans="pairwise coprime"

	n = 333335
	primes = set(range(2, n+1))
	for i in range(2, int(n**0.5+1)):
		primes.difference_update(range(i*2, n+1, i))
	primes=set(primes)

	#print(primes)


	B=set(range(1,333335))
	C=set()
	for i in A:
		a=set()
		while i%2==0:
			a.add(2)
			i//=2
		f=3
		while f*f<=i:
			if i in primes:
				break
			elif i%f==0:
				a.add(f)
				i//=f
			else:
				f+=2
		if i!=1:
			a.add(i)
		B&=a
		if C&a:
			ans="setwise coprime"
		C|=a

	if B:
		ans="not coprime"

	print(ans)





















if __name__ == "__main__":
	main()
