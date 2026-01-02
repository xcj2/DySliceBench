import sys
sys.setrecursionlimit(10000000)
N,X = map(int,input().split())
def n_barg_hight(n):
	if(n == 0):
		return 1

	L1barg_height = n_barg_hight(n-1)
	Lbarg_height = 1 + L1barg_height + 1 + L1barg_height + 1
	return Lbarg_height

def n_barg_pat(n):
	if(n == 0):
		return 1
	L1barg_pat = n_barg_pat(n-1)
	Lbarg_pat = 1 + L1barg_pat*2
	return Lbarg_pat


def answer(N,X):

	if(X == 1):
		if(N == 0):
			return 1
		else:
			return 0
	
	elif(X == n_barg_hight(N)):
		return n_barg_pat(N)

	elif(X == n_barg_hight(N)//2 + 1):
		return n_barg_pat(N-1)+1

	elif(X <= n_barg_hight(N)//2):
		return answer(N-1,X-1)

	elif(X > n_barg_hight(N)//2 + 1):
		Lbarg = n_barg_pat(N-1) + answer(N-1,X-n_barg_hight(N-1)-2) +1
		return Lbarg


print(answer(N,X))