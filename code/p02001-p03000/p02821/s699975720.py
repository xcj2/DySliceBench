import sys
input = sys.stdin.readline
# 昇順ソートされた配列の挿入位置indexを返す O(logN)
from bisect import bisect_left

def isOver(A,n,x):
	cnt = 0
	for a in A:
		cnt += n-bisect_left(A,x-a)
	return cnt

def calOut(A,s,n,x):
	out = 0
	for a in A:
		idx = bisect_left(A,x-a)
		out += s[n]-s[idx]+a*(n-idx)
	return out - (isOver(A,n,x)-m)*x

def calX(A,n,m,l,r):
	while r-l>1:
		# x: 握手で得たい最低パワー値
		x = (l+r)//2
		if isOver(A,n,x) >= m:
			l = x
		else: #握手する限界回数すら満たせないほど大きいxなら
			r = x 
	return l

n,m = map(int, input().split())
A = list(map(int, input().split()))

#累積和の下準備
A.sort()
S = [0]*(n+1)
for i in range(n):
	S[i+1] = S[i]+A[i]

x = calX(A,n,m,A[0]*2,A[n-1]*2)

print(calOut(A,S,n,x))