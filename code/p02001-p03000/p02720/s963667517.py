import numpy as np
K=int(input())

n=np.zeros((10,11),dtype=int)
for i in range(9):
	n[i+1,1]=1
	n[i+1,2]=3
n[9,2]=2

for i in range(3,11):
	n[1,i]=n[2,i-1]+np.sum(n[1,:])+1
	n[2,i]=n[1,i-1]+n[2,i-1]+n[3,i-1]
	n[3,i]=n[4,i-1]+n[2,i-1]+n[3,i-1]
	n[4,i]=n[4,i-1]+n[5,i-1]+n[3,i-1]
	n[5,i]=n[4,i-1]+n[5,i-1]+n[6,i-1]
	n[6,i]=n[5,i-1]+n[6,i-1]+n[7,i-1]
	n[7,i]=n[7,i-1]+n[8,i-1]+n[6,i-1]
	n[8,i]=n[7,i-1]+n[8,i-1]+n[9,i-1]
	n[9,i]=n[8,i-1]+n[9,i-1]

i=1
j=1

def ninecheck(i,j,K,ans):
	for k in range(2):
		K-=n[i-1+k,j]
		if K<=0:
			K+=n[i-1+k,j]
			ans+=(i-1+k)*(10**(j-1))
			if j==1:
				a=ans
				return a
			j-=1
			i=i-1+k
			if i==1:
				a=onecheck(i,j,K,ans)
				return a
			elif i==9:
				a=ninecheck(i,j,K,ans)
				return a
			else:
				a=normalcheck(i,j,K,ans)
				return a

def onecheck(i,j,K,ans):
	K-=1
	if K==0:
		a=ans
		return a
	for k in range(1,j+1):
		K-=n[1,k]
		if K<=0:
			K+=n[1,k]
			ans+=10**(k-1)
			j=k
			if j==1:
				a=ans
				return a
			j-=1
			a=onecheck(i,j,K,ans)
			return a
	i=2
	ans+=i*(10**(j-1))
	j-=1
	a=normalcheck(i,j,K,ans)
	return a

def normalcheck(i,j,K,ans):
	for k in range(3):
		K-=n[i-1+k,j]
		if K<=0:
			K+=n[i-1+k,j]
			ans+=(i-1+k)*(10**(j-1))
			if j==1:
				a=ans
				return a
			j-=1
			i=i-1+k
			if i==1:
				a=onecheck(i,j,K,ans)
				return a
			elif i==9:
				a=ninecheck(i,j,K,ans)
				return a
			else:
				a=normalcheck(i,j,K,ans)
				return a



ans=0
while True:
	K-=n[i,j]
	if K<=0:
		ans+=i*(10**(j-1))
		K+=n[i,j]
		if j==1:
			b=ans
			break
		j-=1
		if i==1:
			b=onecheck(i,j,K,ans)
			break
		elif i==9:
			b=ninecheck(i,j,K,ans)
			break
		else:
			b=normalcheck(i,j,K,ans)
			break
	if i==9:
		i=1
		j+=1
	else:
		i+=1
		continue




print(b)