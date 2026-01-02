
def bubblesort(c, n):
	for i in range(n):
		for j in range(n-1, 0, -1):
			if (c[j][1] < c[j-1][1]):
				c[j], c[j-1] = c[j-1], c[j]

def selectionsort(c, n):
	for i in range(n):
		minj = i
		for j in range(i, n):
			if (c[j][1] < c[minj][1]):
				minj = j
		c[i], c[minj] = c[minj], c[i]

def output(c):
	for i in range(len(c)):
		if i != 0: print(" ", end="")
		print("{}{}".format(c[i][0], c[i][1]), end="")
	print()

def main():
	n = int(input())
	data = input().split()
	cards = []

	for c in data:
		cards.append((c[0],int(c[1])))
	cards1 = cards[:]
	cards2 = cards[:]

	bubblesort(cards1, n)
	output(cards1)
	print("Stable")

	selectionsort(cards2, n)
	output(cards2)
	if (cards1 == cards2):
		print("Stable")
	else:
		print("Not stable")

if __name__ == "__main__":
	main()