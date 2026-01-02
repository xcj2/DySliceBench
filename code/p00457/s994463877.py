def cara(n):
	kazu=[]
	ilo=[]
	a=int(input())
	una=a
	kazu.append(1)
	ilo.append(a)
	for n in range(n-1):
		a=int(input())
		if una==a:
			kazu[-1]+=1
		else:
			kazu.append(1)
			ilo.append(a)
			una=a
	return ilo,kazu
def kes(ilo,kazu):
	k=10000
	unanseer=sum(kazu)
	anseer=sum(kazu)
	for p in range(len(ilo)):
		n=0
		if kazu[p]>=3 :
			anseer=kurabe(ilo,kazu,p)
		n=0
		if p+2 < len(ilo) and ilo[p]==ilo[p+2] and kazu[p]+kazu[p+2]>=3 and kazu[p+1]==1:
			while p+2+n<len(ilo) and p-n>=0 and ilo[p-n]==ilo[p+2+n] and kazu[p-n]+kazu[p+2+n]>=4:
				n+=1
			if n>2500:
				print(n)
			unanseer=kensa(ilo,kazu,n,p)
		if unanseer<anseer:
			anseer=unanseer
		if anseer<k: 
			k=anseer
	return k
def kensa(ilo,kazu,n,p):
	k=0
	if n==0:
		for w in range(len(kazu)):
			k+=kazu[w]
	else:
		for q in range(0,p-n+1):
			k+=kazu[q]
		for i in range(p+2+n,len(kazu)):
			k+=kazu[i]
	return k
def kurabe(ilo,kazu,p):
	n=0
	a=0
	b=0
	k=0
	
	#上からもらう
	if p+1 < len(ilo):
		kazu[p+1]-=1
		kazu[p]+=1
		while 0<p-a and len(kazu)>p+1+a and ilo[p+1+a]==ilo[p-1-a] and kazu[p+1+a]+kazu[p-1-a]>=4:
			a+=1
		kazu[p+1]+=1
		kazu[p]-=1

	#下からもらう
	if p-1 >= 0:
		kazu[p-1]-=1
		kazu[p]+=1
		while len(kazu)>p+1+b and 0<p-b and ilo[p+b+1]==ilo[p-1-b] and kazu[p+b+1]+kazu[p-1-b]>=4:
			b+=1
		kazu[p-1]+=1
		kazu[p]-=1
	if a<b:
		n=b
	else:
		n=a
	for q in range(0,p-n):
			k+=kazu[q]
	for i in range(p+n,len(kazu)):
			k+=kazu[i]
	k-=3
	return k

while True:
	n=int(input())
	if n==0:
		break
	ilo,kazu=cara(n)
	print(kes(ilo,kazu))
