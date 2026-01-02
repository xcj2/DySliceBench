from typing import List


class Trump:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return self.suit + str(self.value)


def bubble(C: List[Trump], N: int) -> None:
	for i in range(N):
		for j in range(N-1, i, -1):
			if C[j].value < C[j-1].value:
				C[j], C[j-1] = C[j-1], C[j]
	print(*C)


def selection(C: List[Trump], N: int) -> None:
	for i in range(N):
		minj = i
		for j in range(i, N):
			if C[j].value < C[minj].value:
				minj = j
		C[i], C[minj] = C[minj], C[i]
	print(*C)


if __name__ == "__main__":
	N = int(input())
	C1 = []
	for c in input().split():
		C1.append(Trump(int(c[1]), c[0]))
	C2 = C1.copy()

	bubble(C1, N)
	print("Stable")
	selection(C2, N)
	if C1 == C2:
		print("Stable")
	else:
		print("Not stable")
