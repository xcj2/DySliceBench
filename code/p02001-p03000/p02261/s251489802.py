import sys

class Card:
	def __init__(self, card):
		self.card = card
		self.mark = card[0]
		self.value = card[1]
	
	def equals(self, other):
		if self.mark != other.mark: return False
		if self.value != other.value: return False
		return True

	def __str__(self):
		return self.card

def print_cards(cards, cards_):
	n = len(cards)
	same = True
	for i in range(n):
		if cards_ != None and cards[i].equals(cards_[i]) == False:
			same = False
		sys.stdout.write(str(cards[i])) 
		if i != n - 1:
			sys.stdout.write(' ')
	print()
	return same	

def swap(cards, i, j):
	temp = cards[i]
	cards[i] = cards[j]
	cards[j] = temp

def bubble_sort(cards):
	n = len(cards)
	for i in range(n):
		for j in range(n - 1, i, -1):
			if cards[j].value < cards[j - 1].value:
				swap(cards, j, j - 1)

def selection_sort(cards):
	n = len(cards)
	for i in range(n):
		mini = i
		for j  in range(i, n):
			if cards[j].value < cards[mini].value:
				mini = j
		if mini != i:
			swap(cards, i, mini)
		
n = int(input())
input_list = list(map(str, input().split()))
cards1 = [None] * n
cards2 = [None] * n
for i in range(n):
	cards1[i] = Card(input_list[i])
	cards2[i] = Card(input_list[i])
	
bubble_sort(cards1)
selection_sort(cards2)

print_cards(cards1, None)
print('Stable')

stable = print_cards(cards2, cards1)
if stable == True:
	print('Stable')
else:
	print('Not stable')

