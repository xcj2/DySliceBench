N = int(input())
array = list(input().split())
array2 = array[:]
array3 = array[:]

def bubble_sort(array, N):
	flag = 1
	i = 0
	while flag:
		flag = 0 
		j = N-1
		while j > i:
			if array[j][1] < array[j-1][1]:
				array[j], array[j-1] = array[j-1], array[j]
			j -= 1
			flag = 1
		i += 1


def selection_sort(array, n):
	for i in range(n):
		minij = i 
		for j in range(i, n):
			if array[j][1] < array[minij][1]:
			    minij = j 
		array[i], array[minij] = array[minij], array[i]

def is_stable(Input, output, n):
	for i in range(n):
		for j in range(i+1, n):
			for a in range(n):
				for b in range(a+1, n):
					if Input[i][1] == Input[j][1] and Input[i] == output[b] and Input[j] == output[a]:
						return False
	return True 

bubble_sort(array, N)
print(' '.join(array))
print('Stable')
selection_sort(array2,N)
print(' '.join(array2))
if is_stable(array3, array2, N):
	print('Stable')
else:
	print('Not stable')





