def all_same(a):
    return all([x==a[0] for x in a])

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

def primechecker(x):
	original=x
	primefactorization=set()
	for i in range (2,int(original**0.5)+1):
		while x%i==0:
			primefactorization.add(i)
			x=x//i
	if x>1:
		primefactorization.add(x)
	return primefactorization

primefactors=set()

N=int(input())
array=[int(x) for x in input().split()]
checklist=[]
totality=0

def pairwisecoprime(array):
	for i in array:
		for j in primechecker(i):
			if j in primefactors:
				return 0
			else:
				primefactors.add(j)
	return 1
if pairwisecoprime(array):
	print("pairwise coprime")
	exit()




for i in array:
	totality=gcd(totality,i)

if totality==1:
	print("setwise coprime")
else:
	print("not coprime")