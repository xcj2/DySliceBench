import cmath
import math

def BITREVERSECOPY(L):
	M=[0]
	n=len(L)
	y=math.log(n,2)
	x=math.ceil(math.log(n,2))
	for i in range(0,x):
		M=[2*e for e in M]
		M+=[e+1 for e in M]
	m=2**x
	N=[0]*m
	L+=[0]*(m-n)
	for i in range(0,m):
		N[i]=L[M[i]]
	return N

def IFFT(L,type):
	P=math.pi						#x=1 for FFT and -1 for IFT
	A=BITREVERSECOPY(L)
	n=len(A)
	x=int(math.log(n,2))
	for i in range(1,x+1):
		m=2**i
		wm=complex(math.cos(2*P/m),type*math.sin(2*P/m))
		for k in range(0,n,m):
			w=1
			for j in range(0,m//2):
				t=w*A[k+j+m//2]
				u=A[k+j]
				A[k+j]=(u+t)
				A[k+j+m//2]=(u-t)
				if(type==-1):
					A[k+j]/=2
					A[k+j+m//2]/=2
				w=w*wm
			
	return A


def fftmultiplymodp(A,B,p):
	m=len(A)
	n=len(B)
	r=0
	while(2**r<m+n):
		r+=1
	b=2**r
	A=A+(b-m)*[0]
	B=B+(b-n)*[0]
	l=len(A)
	base=math.ceil(math.sqrt(p))
	rem=(base*base)%p
	C=[0]*l
	D=[0]*l
	E=[0]*l
	F=[0]*l
	G=[0]*l
	H=[0]*l
	Z=[0]*l

	for i in range(0,l):
		x=A[i]
		y=B[i]
		C[i]=x//base
		D[i]=y//base
		A[i]=x%base
		B[i]=y%base

	g=lambda x:(round(x.real))%p
	X=IFFT(A,1)
	Y=IFFT(B,1)
	X1=IFFT(C,1)
	Y1=IFFT(D,1)
	for i in range(0,l):
		E[i]=X[i]*Y[i]
		F[i]=X[i]*Y1[i]
		G[i]=X1[i]*Y[i]
		H[i]=X1[i]*Y1[i]
		
	E=list(map(g,IFFT(E,-1)))
	F=list(map(g,IFFT(F,-1)))
	G=list(map(g,IFFT(G,-1)))
	H=list(map(g,IFFT(H,-1)))
	

	for i in range(0,l):
		Z[i]=(E[i]+base*(F[i]+G[i])+rem*H[i])%p
	
	return Z


class Polynomial:
	def __init__(self,L,mod):
		self.poly=L
		self.mod=mod

	def __str__(self):
		return str(self.poly)

	def __add__(self,other):
		L=self.poly
		M=other.poly
		p=self.mod
		if(p!=other.mod):
			return "Check your inputs"
		else:
			l=len(L)
			m=len(M)
			if(l==m):
				ans=[0]*l
				for i in range(0,l):
					ans[i]=(L[i]+M[i])%p
			elif(l<m):
				ans=[0]*m
				for i in range(0,l):
					ans[i]=(L[i]+M[i])%p
				for i in range(l,m):
					ans[i]=M[i]%p
			else:
				ans=[0]*l
				for i in range(0,m):
					ans[i]=(L[i]+M[i])%p
				for i in range(m,l):
					ans[i]=(L[i])%p

			return Polynomial(ans,p)

	def __sub__(self,other):
		L=self.poly
		M=other.poly
		l=len(L)
		m=len(M)
		p=self.mod
		if(p!=other.mod):
			return "Check your inputs"
		else:
			if(l==m):
				ans=[0]*l
				for i in range(0,l):
					ans[i]=(L[i]-M[i])%p
			elif(l<m):
				ans=[0]*m
				for i in range(0,l):
					ans[i]=(L[i]-M[i])%p
				for i in range(l,m):
					ans[i]=(-1*M[i])%p
			else:
				ans=[0]*l
				for i in range(0,m):
					ans[i]=(L[i]-M[i])%p
				for i in range(m,l):
					ans[i]=(L[i])%p

			return Polynomial(ans,p)


	def normalize(self):
		L=self.poly
		p=self.mod
		l=len(L)
		i=l-1
		if(L[i]==0):
			while(L[i]==0):
				i-=1
			return L[:i+1]
		return Polynomial(L,p)

	
	def __mul__(self,other):
		L=self.poly
		M=other.poly
		if(min(len(L),len(M))==0):
			return Polynomial([0])
		else:
			return self.fftmultiply(other)

	def fftmultiply(self,other):
		L=self.poly
		M=other.poly
		p=self.mod
		N=fftmultiplymodp(L,M,p)
		return Polynomial(N,p)
	

	def modxk(self,k):
		L=self.poly
		p=self.mod
		if(len(L)<=k):
			return Polynomial(L,p)
		else:
			return Polynomial(L[:k],p)

	def inverse(self,n):
		L=self.poly
		p=self.mod
		l=len(L)
		ans=Polynomial([1/L[0]],p)
		M=Polynomial([2],p)
		a=1
		while(a<n):			
			C=M-(self.modxk(2*a)*ans).modxk(2*a)
			ans=(ans*C).modxk(2*a)				
			a*=2
		return ans.modxk(n)


s=int(input())
P=Polynomial([1,-1,0,-1],10**9+7)
M=P.inverse(s-2).poly
if(len(M)<1):
	print(0)
else:
	print(int(M[-1]))
