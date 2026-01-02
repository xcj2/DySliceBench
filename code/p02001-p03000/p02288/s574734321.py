from typing import List

def parent(i: int) -> int:
	return i // 2

def left(i: int) -> int:
	return 2 * i

def right(i: int) -> int:
	return 2 * i + 1


def maxHeapify(A: List[int], i: int) -> None:
	l = left(i)
	r = right(i)
	if l <= H and A[l] > A[i]:
		largest = l
	else:
		largest = i
	if r <= H and A[r] > A[largest]:
		largest = r
	
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		maxHeapify(A, largest)

def buildMaxHeap(A: List[int]) -> None:
	for i in range(H//2, 0, -1):
		maxHeapify(A, i)


if __name__ == "__main__":
	H = int(input())
	A = [None] + list(map(int, input().split()))
	buildMaxHeap(A)
	for i in range(1, H + 1):
		print(f" {A[i]}", end="")
	print()
