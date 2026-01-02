import sys
readline = sys.stdin.buffer.readline

mod=998244353

class BIT:
	def __init__(self,n):
		self.n=n
		self.buf=[0]*n
	
	def add(self,i,v):
		buf=self.buf
		while i<n:
			buf[i]+=v
			if buf[i]>=mod:
				buf[i]-=mod
			i+=(i+1)&(-i-1)
	
	def get(self,i):
		buf=self.buf
		res=0
		while i>=0:
			res+=buf[i]
			if res>=mod:
				res-=mod
			i-=(i+1)&(-i-1)
		return res
	
	def rng(self,b,e):
		res=self.get(e-1)-self.get(b)
		if res<0:
			res+=mod
		return res

n,k=map(int,readline().split())
p=list(map(int,readline().split()))
for i in range(n):
	p[i]-=1

ans=0

bit=BIT(n)
for i in range(n):
	ans+=i-bit.get(p[i])
	bit.add(p[i],1)

z=pow(2,mod-2,mod);
w=1
winv=1
rem=(k-1)*pow(k,mod-2,mod)%mod
reminv=pow(rem,mod-2,mod)

bit=BIT(n)
for i in range(n):
	lw=bit.get(p[i])
	up=bit.rng(p[i],n)
	dif=(lw-up+mod)%mod
	ans=(ans+dif*w*z)%mod
	bit.add(p[i],winv)
	if i>=k-1:
		w=w*rem%mod
		winv=winv*reminv%mod

print(ans)
