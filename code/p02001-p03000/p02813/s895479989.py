n = int(input())
p = [i for i in map(int, input().split())]
q = [i for i in map(int, input().split())]

sorted_list = sorted(p)
all_list = []

def listExcludedIndices(data, indices=[]):
	return [x for i, x in enumerate(data) if i not in indices]

def permutationListRecursive(data, r):
	if r <= 0 or r > len(data):
		return []
	
	result = []
	_permutationListRecursive(data, r, [], result)
	return result

def _permutationListRecursive(data, r, progress, result):
	if r == 0:
		result.append(progress)
		return
	
	for i in range(len(data)):
		_permutationListRecursive(listExcludedIndices(data, [i]), r - 1, progress + [data[i]], result)


a = -1
b = -1

for i, list_ in enumerate(permutationListRecursive(sorted_list, n)):
	#print(list_)
	if list_ == p:
		a = i

	if list_ == q:
		b = i

	if a != -1 and b != -1:
		break

print(abs(a-b))
