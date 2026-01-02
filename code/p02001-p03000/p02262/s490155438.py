import copy

def insertionSort(A,n,g,cnt):

	for i in range(g,n):
		v = A[i]
		j = i - g
		while j >= 0 and A[j] > v:
			A[j+g] = A[j]
			j = j - g
			cnt[0] += 1
		A[j+g] = v

def shellSort(A,n,cnt):

	G = []

	#Creating h array
	h = 1
	while True:
		if h > n:
			break
		G.append(h)
		h = 3*h + 1

	# Calling insertionSort
	for i in range(len(G)-1,-1,-1):
		insertionSort(A,n,G[i],cnt)

	return G

def test():

	A = []
	cnt = []
	n = int(input())

	cnt.append(0)
	for i in range(n):
		tmp = int(input())
		A.append(tmp)

	G = shellSort(A,n,cnt)

	print(len(G))
	for i in range(len(G)-1,0,-1):
		print(f"{G[i]} ",end='')
	print(f"{G[0]}")

	print(cnt[0])
	for i in range(n):
		print(A[i])

if __name__ == "__main__":
	test()

