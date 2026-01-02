MAXN = 1000001
spf = [i for i in range(MAXN)] 
hash1 = [0 for i in range(MAXN)] 

def sieve(): 
	for i in range(4, MAXN, 2): 
		spf[i] = 2

	for i in range(3, MAXN): 
		if i * i > MAXN: 
			break
		if (spf[i] == i): 
			for j in range(i * i, MAXN, i): 
				if (spf[j] == j): 
					spf[j] = i 

def getFactorization(x): 

	while (x != 1): 
		temp = spf[x] 
		if (x % temp == 0): 

			hash1[spf[x]] += 1
			x = x // spf[x] 

		while (x % temp == 0): 
			x = x // temp 

def hasValidNum(arr, n): 

	sieve() 

	for i in range(n): 
		getFactorization(arr[i]) 

	for i in hash1:
		if(i>1):
			return False
	return True

def gcd(a,b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b) 

n=int(input())
arr=list(map(int,input().split()))
if (hasValidNum(arr, n)): 
	print("pairwise coprime") 
else: 
	g=arr[0]
	for i in range(1,n):
		g=gcd(g,arr[i])
	if(g==1):
		print("setwise coprime") 
	else:
		print("not coprime")