import sys
def input():
	return sys.stdin.readline()[:-1]

def included(x):
	if x == "AB":
		return 0, 1
	elif x == "BC":
		return 1, 2
	else:
		return 0, 2

def ans(x):
	l = ["A", "B", "C"]
	return l[x]

n, a, b, c = map(int, input().split())
nums = [a, b, c]
s = [input() for _ in range(n)]
res = []
for i, x in enumerate(s):
	y, z = included(x)
	if nums[y] == nums[z] == 0:
		print("No")
		break
	if i == n-1:
		if nums[y] >= nums[z]:
			res.append(ans(z))
		elif nums[z] > nums[y]:
			res.append(ans(y))
	else:
		if nums[y] > nums[z]:
			res.append(ans(z))
			nums[y] -= 1
			nums[z] += 1
		elif nums[z] > nums[y]:
			res.append(ans(y))
			nums[z] -= 1
			nums[y] += 1
		elif z in included(s[i+1]):
			res.append(ans(z))
			nums[y] -= 1
			nums[z] += 1
		else:
			res.append(ans(y))
			nums[z] -= 1
			nums[y] += 1
else:
	print("Yes")
	print(*res, sep="\n")