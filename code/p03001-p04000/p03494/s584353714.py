import sys
sys.setrecursionlimit(10**8)

def sort(a):
	a.sort()

def rev(a):
	a.reverse()

def sd():
	return int(input())

def _sd():
	return map(int,input().split())


def ss():
	return input()

def sf():
	return float(input())

def dfs():
		# write dfs code here. And delete pass.
		pass

def bfs():
		# write bfs code here. And delete pass.
		pass
 
def main():
	f=bool(False)
	ans = int(0)
	N=sd()
	A=list(map(int,input().split()))
	while(1):
		for i in range(N):
			if A[i]%2:
				f=True
			else : 
				A[i]/=2
		if(not f):
			ans+=1
		else:
			break
	print(ans)

main()