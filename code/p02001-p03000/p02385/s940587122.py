dice = [
	[1, 2, 4, 3, 5],
	[5, 2, 0, 3, 4],
	[1, 5, 4, 0, 3],
	[1, 0, 4, 5, 2],
	[0, 2, 5, 3, 1],
	[1, 3, 4, 2, 0]
]

def getRound(D, top):
	result = []
	for index in dice[top]:
		result.append(D[index])
	return result

def compareRound(l1, l2):
	if l1[4] != l2[4]:
		return False
	elif l1[0] not in l2:
		return False
	offset = l2.index(l1[0])
	
	for i in range(4):
		if l1[i] != l2[(i+offset)%4]:
			return False
	return True

def compare(D1, D2, i1):
	if D1[i1] not in D2:
		return False
	i2 = D2.index(D1[i1])
	return compareRound(getRound(D1, i1), getRound(D2, i2))

D1 = input().split(" ")
D2 = input().split(" ")
isSame = False
for i in range(6):
	if compare(D1, D2, i):
		isSame = True
if isSame:
	print("Yes")
else:
	print("No")