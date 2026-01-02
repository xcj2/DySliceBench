import sys

class Card:
	def __init__(self, card):
		self.card = card
		self.mark = card[0]
		self.value = int(card[1])

	def __str__(self):
		return self.card

def print_cards(arr_print, arr_compare):
	n = len(arr_print)
	same = True
	for i in range(n):
		if arr_compare != None and arr_print[i].card != arr_compare[i].card: same = False
		sys.stdout.write(str(arr_print[i]))
		if i != n - 1:
			sys.stdout.write(' ')
	print()
	return same

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

print_cards(cards1, None)
print('Stable')

stable = print_cards(cards2, cards1)
if stable == True:
	print('Stable')
else:
	print('Not stable')

