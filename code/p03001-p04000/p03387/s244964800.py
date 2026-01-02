numList = input().split()
numList = list(map(int, numList))
commandList = [
	[2,0,0],
	[0,2,0],
	[0,0,2],
	[0,1,1],
	[1,0,1],
	[1,1,0]
]
numListList = [numList]

def search(depth):
	global numListList
	tmpList = []
	for numList in numListList:
		for command in commandList:
			sumedList = sumList(numList, command)
			if check(sumedList, depth+1):
				return
			tmpList.append(sumedList)
	numListList = tmpList
	search(depth+1)

def sumList(list1, list2):
	return [list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2]]

def check(numList, count):
	if numList[0] == numList[1] and numList[1] == numList[2]:
		print(count)
		return True

	if numList[0] == numList[1]:
		return check2(numList[0], numList[2], count)

	if numList[1] == numList[2]:
		return check2(numList[1], numList[0], count)

	if numList[0] == numList[2]:
		return check2(numList[0], numList[1], count)

	return False

def check2(num1, num2, count):
	if num1 > num2:
		if (num1-num2)%2 == 0:
			print(int(count+(num1-num2)/2))
			return True
		else:
			print(int(count+(num1-num2)/2)+2)
			return True
	else:
		print(int(count+(num2-num1)))
		return True

if check(numList, 0):
	pass
else:
	search(0)