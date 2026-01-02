import math

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def best_alignment(lst, small):

	ans = 0

	p = []

	if(small):
		p.append(lst[-1])
		p.append(lst[-1])
		del lst[-1:]
	else:
		m = min(lst)
		p.append(lst[0])
		p.append(lst[0])
		lst.pop(0)


	while(len(lst)>0):

		if(small):
			ans = ans + abs(max(p)-lst[0])
			if(len(lst)==1):
				break

			ans = ans + abs(min(p)-lst[1])

			p = []
			p.append(lst.pop(0))
			p.append(lst.pop(0))
			small = False
			continue
		else:
			ans = ans + abs(min(p)-lst[-1])
			if(len(lst)==1):
				break

			ans = ans + abs(max(p)-lst[-2])

			p = []
			p.append(lst[-1])
			p.append(lst[-2])
			del lst[-2:]
			small = True
			continue

	return ans	




N = int(input().strip())
A = []
for i in range(N):
	A.append(int(input().strip()))

A.sort()
A_=A.copy()

print(max(best_alignment(A, True), best_alignment(A_, False)))