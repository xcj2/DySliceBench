from math import sqrt
def get_divisor(num):
	arr = [i for i in range(1,int(sqrt(num))+1) if num % i == 0]
	arr += [num // i for i in reversed(arr) if num // i not in arr]
	return arr

def get_common(num1, num2):
	list_a = get_divisor(num1)
	list_b = get_divisor(num2)
	return [i for i in list_a if i in list_b]

def prime_ch(num):
	if num == 1:
		return False
	for i in list(range(2,int(sqrt(num))+1)):
		if num % i == 0:
			return False
	return True


A,B = list(map(int,input().split()))[:2]
common = get_common(A,B)
c_prime = [p for p in common if prime_ch(p)]
print((len(c_prime)+1))