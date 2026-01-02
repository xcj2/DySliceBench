a,b = map(int,input().split())

def make_divisors(n):
	divisors = []
	for i in range(1, int(n**0.5)+1):
		if n % i == 0:
			divisors.append(i)
			if i != n // i:
				divisors.append(n//i)
	# divisors.sort()
	return divisors

def gcd(x,y):
	while y!=0:
		x,y=y,x%y
	return x

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

#factorization(24)
## [[2, 3], [3, 1]]
##  24 = 2^3 * 3^1

g = gcd(a,b)
#gcd_list = make_divisors(g)
bunkai = factorization(g)

if len(bunkai) == 1 and bunkai[0][0] == 1:
	print(1)
else:
	print(len(bunkai) + 1 )
