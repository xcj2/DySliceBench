class Card:
        def __init__(self, suit, num):
                self.suit = suit
                self.num = num

def bubbleSort(C, N):
        for i in range(N): 
                for j in range(N - 1, i, -1):
                        if C[j].num < C[j - 1].num:
                                C[j].num, C[j - 1].num = C[j - 1].num, C[j].num
                                C[j].suit, C[j - 1].suit = C[j - 1].suit, C[j].suit

def selectionSort(C, N):
        for i in range(N):
                minID = i
                for j in range(i, num):
                        if C[j].num  < C[minID].num:
                                minID = j
                C[i].num, C[minID].num = C[minID].num, C[i].num
                C[i].suit, C[minID].suit = C[minID].suit, C[i].suit

num = int(input())
list = input().split()

cardListA = []
cardListB = []
sortA = []
sortB = []

isSame = True

for i in range(num):
        cardListA.append(Card(list[i][0], list[i][1]))
        cardListB.append(Card(list[i][0], list[i][1]))

bubbleSort(cardListA, num)
selectionSort(cardListB, num)


for i in range(num):
        sortA.append(cardListA[i].suit + cardListA[i].num)
        sortB.append(cardListB[i].suit + cardListB[i].num)
        if sortA[i] != sortB[i]:
                isSame = False

print(" ".join(sortA))
print("Stable")
print(" ".join(sortB))
if isSame:
        print("Stable")
else:
        print("Not stable")
