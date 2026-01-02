import copy 
n = int(input())
#*L, = map(str, input().split())
#L = [int(i) for i in input().split()]
*L, = input().split()

A1 = copy.copy(L)
A2 = copy.copy(L)

def bubble_sort(A,N):
	for i in range(N):
		for j in reversed(range(i+1,N)):
			if int(A[j][1]) < int(A[j-1][1]):
				key = A[j]
				A[j] = A[j-1]
				A[j-1] = key
				#print("b",A)

"""
for i in range(N):
	for j in reversed(range(i+1,N)):
		if int(A[j][1]) < int(A[j-1][1]):
			key = A
			A[j] = A[j][0] + A[j-1][1]
			A[j-1] = key[j-1][0] + key[j][1]
			print(A)
"""


def selection_sort(A,N):
	for i in range(N):
		minj = i
		for j in range(i,N):
			if A[j][1] < A[minj][1]:
				minj = j
		if A[i][1] > A[minj][1]:
			key = A[i]
			A[i] = A[minj]
			A[minj] = key
			#print(A)

"""
def isStable(input,output):
	for i in range(len(inp)):
		if inp[i][1] == oup[i][1] and inp[i][0] != oup[i][0]:
			#print("False")
			return False
		else:
			True
"""



"""
if inp[i][1] == oup[i][1] and inp[i][0] != oup[i][0]:
	print("False")

print(inp[i][1])
print(oup[i][1])
print(inp[i][0])
print(oup[i][0])
"""

bubble_sort(A1,n)
selection_sort(A2,n)

print(*A1)
print("Stable")
print(*A2)
if A1 == A2:
	print("Stable")
else:
	print("Not stable")




