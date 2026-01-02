N = int(input())
data = {}
bits = 0
bit_table = [set() for _ in range(31)]
for a in map(int, input().split()):
	bits |= a
	if a in data:
		data[a] += 1
	else:
		data[a] = 1
	i = 0
	b = a
	while b:
		if b % 2 == 1:
			bit_table[i].add(a)
		b //= 2
		i += 1

def pop(data, a):
	if a in data:
		if data[a] == 1:
			del data[a]
		else:
			data[a] -= 1
		return a
	else:
		return None

def check2(data0, a1, a2):
	if (a1 | a2) != bits:
		return False
	
	data = { k: data0[k] for k in data0 }
	a0 = a1
	pop(data, a1)
	pop(data, a2)
	
	while data:
		a3 = a1 ^ a2
		a4 = pop(data, a3)
		if a4 == None:
			return False
		a1 = a2
		a2 = a3
	return a0 == (a1 ^ a2)

def check(data):
	keys = list(data.keys())
	a1 = keys[0]
	b = bits & (~a1)
	cands = set(keys)
	i = 0
	while b:
		if b % 2 == 1:
			cands &= bit_table[i]
		b //= 2
		i += 1
	
	for a2 in cands:
		if a1 != a2 or data[a1] > 1:
			if check2(data, a1, a2):
				return True
	return False

if check(data):
	print("Yes")
else:
	print("No")
