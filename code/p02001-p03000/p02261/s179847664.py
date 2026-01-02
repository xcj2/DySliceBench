import copy

def Bubble_Sort(n,cards):

	for i in range(n):
		for j in range(n-1,i,-1):
			if int(cards[j][1]) < int(cards[j-1][1]):
				cards[j],cards[j-1] = cards[j-1],cards[j]

def Selection_Sort(n,cards):

	for i in range(n):
		mini = i
		for j in range(i,n):
			if int(cards[j][1]) < int(cards[mini][1]):
				mini = j
		cards[i],cards[mini] = cards[mini],cards[i]

def Print_cards(n,cards):

	for i in range(n-1):
		print(f"{cards[i][0]}{cards[i][1]} ",end='')
	print(f"{cards[n-1][0]}{cards[n-1][1]}")


def isStable(n,original,sorted):

	for i in range(n):
		for j in range(i+1,n):
			for a in range(n):
				for b in range(a+1,n):
					if int(original[i][1]) == int(original[j][1]) and original[i] == sorted[b] and original[j] == sorted[a]:
						return False

	return True

def test():

	n = int(input())
	cards_original = input().split()
	cards_for_Bubble = copy.deepcopy(cards_original)
	cards_for_Selection = copy.deepcopy(cards_original)

	Bubble_Sort(n,cards_for_Bubble)
	Print_cards(n,cards_for_Bubble)
	if isStable(n,cards_original,cards_for_Bubble) == True:
		print("Stable")
	else:
		print("Not stable")

	Selection_Sort(n,cards_for_Selection)
	Print_cards(n,cards_for_Selection)
	if isStable(n,cards_original,cards_for_Selection) == True:
		print("Stable")
	else:
		print("Not stable")

if __name__ == "__main__":
	test()


