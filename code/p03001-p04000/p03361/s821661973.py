h, w = (int(i) for i in input().split())
list = []

for i in range(h):
	list.append([])
	row = input()
	for j in range(w):
		element = row[j]
		list[i].append(element == '#')

def all_check(h, w, list):
	for i in range(h):
		for j in range(w):
			if not check(i, j, h, w, list):
				return False

	return True

def check(i, j, h, w,list):
	if list[i][j]:
		return subcheck(i, j, h, w, list)
	else:
		return True

def subcheck(i, j, h, w, list):
	if i > 0 and list[i-1][j]:
		return True
	if i < h-1 and list[i+1][j]:
		return True
	if j > 0 and list[i][j-1]:
		return True
	if j < w-1 and list[i][j+1]:
		return True

if all_check(h, w, list):
	print("Yes")
else:
	print("No")