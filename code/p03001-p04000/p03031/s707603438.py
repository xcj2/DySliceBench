import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline


def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))

# mod=10**9+7
# rstrip().decode('utf-8')


def main():
	n,m=MI()
	ks=[LI() for _ in range(m)]
	s=[i[1:] for i in ks]
	p=LI()
	ans=0

	for i in range(1<<n):
		li=[0]*m
		for j in range(n):
			for k in range(m):
				if 1&i>>j:
					if j+1 in s[k]:
						li[k]=1-li[k]
		if p==li:
			ans+=1
	print(ans)










if __name__ == "__main__":
	main()
