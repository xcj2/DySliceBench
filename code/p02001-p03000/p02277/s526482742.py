INF = 1000000000

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return self.suit + ' ' + str(self.value)


def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j].value <= x.value:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1



def quickSort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quickSort(A, p, q - 1)
		quickSort(A, q + 1, r)


def merge(A, left, mid, right):
	L = A[left:mid]
	R = A[mid:right]
	L.append(Card("INF", INF))
	R.append(Card("INF", INF))
	i = 0
	j = 0
	for k in range(left, right):
		if L[i].value <= R[j].value:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1


def mergeSort(A, left, right):
	if left + 1 < right:
		mid = (left + right) // 2
		mergeSort(A, left, mid)
		mergeSort(A, mid, right)
		merge(A, left, mid, right)


if __name__ == "__main__":
	n = int(input())
	A = []
	for _ in range(n):
		suit, value = input().split()
		A.append(Card(suit, int(value)))

	B = A.copy()
	quickSort(A, 0, n - 1)
	mergeSort(B, 0, n)
	if A == B:
		print("Stable")
	else:
		print("Not stable")
	for card in A:
		print(card)
