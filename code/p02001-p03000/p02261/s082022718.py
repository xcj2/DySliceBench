import sys

class Card:
	def __init__(self, card):
		self.card = card
		self.mark = card[0]
		self.value = int(card[1])

	def __str__(self):
		return self.card

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def bubble_sort(arr):
	n = len(arr)
	for i in range(0, n):
		for j in range(n - 1, i, -1):
			if arr[j].value < arr[j - 1].value:
				swap(arr, j, j - 1)

def selection_sort(arr):
	n = len(arr)
	for i in range(n):
		minj = i
		for j in range(i, n):
			if arr[j].value < arr[minj].value:
				minj = j
		if minj != i:
			swap(arr, i, minj)

n = int(input())
arr = list(map(str, input().split()))
cards1 = [None] * n
cards2 = [None] * n
for i in range(n):
	cards1[i] = Card(arr[i])
	cards2[i] = Card(arr[i])

bubble_sort(cards1)
selection_sort(cards2)

for i in range(n):
	sys.stdout.write(cards1[i].card)
	if i != n - 1:
		sys.stdout.write(' ')
print()
print('Stable')

stable = True
for i in range(n):
	if cards1[i].card != cards2[i].card: stable = False
	sys.stdout.write(cards2[i].card)
	if i != n - 1:
		sys.stdout.write(' ')
print()
if stable == True:
	print('Stable')
else:
	print('Not stable')

