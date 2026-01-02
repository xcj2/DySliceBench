def BubbleSort(C,n):
	for i in range(n):
		for j in range(i+1,n)[::-1]:
			if C[j][1] < C[j-1][1]:
				C[j],C[j-1] = C[j-1],C[j]
	return C

def SelectionSort(C,n):
	for i in range(n):
		minj = i
		for j in range(i,n):
			if C[j][1] < C[minj][1]:
				minj = j
		C[i],C[minj] = C[minj],C[i]
	return C

def stable(C):
	new = []
	for i in range(1,10):
		Ci = [cc for cc in C if cc[1]==str(i)]
		new += Ci
	return new

n = int(input())
C = input().split()
x,y,z = C[:],C[:],C[:]
bubble = BubbleSort(x,n)
selection = SelectionSort(y,n)
sta = stable(z)

print(' '.join(bubble))
print({True:'Stable',False:'Not stable'}[sta==bubble])
print(' '.join(selection))
print({True:'Stable',False:'Not stable'}[sta==selection])