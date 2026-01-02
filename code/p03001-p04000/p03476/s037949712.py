import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
#input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

#2335

def main():
	n = 10**5+10
	primes = set(range(2, n+1))
	for i in range(2, int(n**0.5+1)):
		primes.difference_update(range(i*2, n+1, i))

	li=set()
	for i in primes:
		li.add(i)
		if i*2<n:
			li.add(i*2)
	li=list(li)
	li.sort()
	#print(li)

	li2=[0]*(n)
	for i in range(len(li)-1):
		if li[i]%2==1 and li[i+1]==li[i]+1:
			li2[li[i]]=1
	#print(li2)

	for i in range(n-1):
		li2[i+1]+=li2[i]
	#print(li2)

	q=II()
	for _ in range(q):
		l,r=MI()
		print(li2[r]-li2[l-1])





if __name__ == "__main__":
	main()