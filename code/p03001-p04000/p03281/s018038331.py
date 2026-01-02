import numpy as np

def unique(w):
    d = {}
    for c in w:
        if c in d.keys():
            d[c] += 1
        else:
            d.setdefault(c, 1)
    return list(d.keys()), list(d.values())

def number_of_divisor(n):
	import numpy as np
	result = []
	while n > 1:
		div = divisor(n)
		result.append(div)
		n //= div
	index, result = unique(result)
	result = [x + 1 for x in result]
	return np.prod(result)

def divisor(n):
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    maxitr = intSqrt(n)
    i = 1
    while True:
        i += 4
        if i > maxitr:
            return n
        elif n % i == 0:
            return i
        i += 2
        if i > maxitr:
            return n
        elif n % i == 0:
            return i

def intSqrt(n):
    x = 1
    while True:
        x2 = (x + n // x) // 2
        if x2 ** 2 <= n and abs(x - x2) <= 1:
            break
        x = x2
    return x2

def ABC106B(n):
    count = 0
    for i in range(3, n+1, 2):
        if number_of_divisor(i) == 8:
            count += 1
    print(count)

n = int(input())
ABC106B(n)
