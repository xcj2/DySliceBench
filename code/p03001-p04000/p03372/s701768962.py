import numpy as np
def hanten(C, X, V):
	return (C*np.ones(X.shape[0])-X)[::-1], V[::-1]

def solv2(N, X, V):
	r = 0
	rbuf = 0
	pos = 0
	Vsum = V.copy()
	for i in range(N):
		rbuf += V[i] - (X[i]-pos)
		pos = X[i]
		if(rbuf > r):
			r = rbuf
		Vsum[i] = r
	return Vsum

def solv(N, C, X, V):
	r = 0
	rbuf1 = 0
	pos = 0
	ibuf = 0
	iX, iV = hanten(C, X, V) 
	iv = solv2(N, iX, iV)
	#print(iv)
	for i in range(N):
		rbuf1 += V[i] - 2*(X[i]-pos)
		rbuf2 = iv[N-(i+2)]
		if(i == N-1):
			rbuf2 = 0
		rbuf = rbuf1 + rbuf2
		pos = X[i]
		#print(rbuf, rbufbuf)
		if(rbuf > r):
			r = rbuf
	return max(r, iv[-1])
	
def main():
	buf = input().split()
	N = int(buf[0])
	C = int(buf[1])
	X = np.zeros(N)
	V = np.zeros(N)
	for i in range(N):
		buf = input().split()
		X[i] = int(buf[0])
		V[i] = int(buf[1])
	r1 = solv(N, C, X, V)
	X, V = hanten(C, X, V)
	r2 = solv(N, C, X, V)
	print(int(max(r1, r2)))
	#print(solv2(N, X, V))
main()# your code goes here