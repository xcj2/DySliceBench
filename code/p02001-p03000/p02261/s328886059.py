def selectionSort(arr):
	icnt = 0
	for i in range(0, len(arr)):
		imin = i
		for j in range(i + 1, len(arr)):
			if arr[j][1] < arr[imin][1]:
				#			if arr[j] < arr[imin]:
				imin = j
		if imin != i:
			arr[i], arr[imin] = arr[imin], arr[i]
			icnt = icnt + 1


def bubbleSort(arr):
	flg = True
	cnt = 0
	while flg:
		flg = False
		for i in range(len(arr) - 1, 0, -1):
			if arr[i][1] < arr[i - 1][1]:
				#			if arr[i] < arr[i - 1]:
				arr[i - 1], arr[i] = arr[i], arr[i - 1]
				cnt = cnt + 1
				flg = True

def combine(arr):
	result = ''
	for i in arr:
		result = result + i[0] + str(i[1]) + ' '
	return result.rstrip(' ')

n = int(input())
a = list(input().split())  # [H4, C9, S4, D2, C3]
# a = list(map(int, input().split()))
b = []  # [[H,4], [C,9], [S,4], [D,2], [C,3]]
for i in range(0, len(a)):
	b.append([a[i][0], int(a[i][1])])
c = b.copy()
# c = b

bubbleSort(b)
result_b = combine(b)

selectionSort(c)
result_s = combine(c)

print(result_b)
print('Stable')

print(result_s)
if result_s == result_b:
	print('Stable')
else:
	print('Not stable')


