n = int(input())

sayTable = []
for i in range(n):
	a = int(input())
	
	sayArray = []
	for j in range(a):
		x, y = [int(v) for v in input().split()]
		sayArray.append((x-1, y+1))
	sayTable.append(sayArray)

def countHonest(honest):
	count = 0
	for v in honest:
		if v == 2:
			count += 1
	return count

def checkHonest(sayArray, honest):
	for x, y in sayArray:
		if honest[x] == 0:
				continue
		if y == 2 and honest[x] != 2:
			return False
	return True

def checkHonestAll(sayTable, honest):
	for i in range(n):
		h = honest[i]
		if h != 2:
			continue
		sayArray = sayTable[i]
		for x, y in sayArray:
			if y != honest[x]:
				return False
	return True

def setHonest(sayArray, honest):
	for x, y in sayArray:
		honest[x] = y

def search(sayTable, honest, i):
	if i >= n:
		if checkHonestAll(sayTable, honest):
			return countHonest(honest)
		else:
			return 0

	count = 0
	h = honest[i]
	sayArray = sayTable[i]
	if (h == 0 or h == 2) and checkHonest(sayArray, honest):
		copyHonest = honest[:]
		setHonest(sayArray, copyHonest)
		copyHonest[i] = 2
		c = search(sayTable, copyHonest, i+1)
		if count < c:
			count = c

	honest[i] = 1
	c = search(sayTable, honest, i+1)
	if count < c:
		count = c
	return count

print(search(sayTable, [0] * n, 0))
