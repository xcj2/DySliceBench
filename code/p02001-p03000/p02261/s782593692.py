class Card:
    def __init__(self, info):
        self.suit = info[0]
        self.number = info[1]
    
    def getSuit(self):
        return self.suit
    
    def getNumber(self):
        return self.number
    
    def __repr__(self):
        return self.suit + str(self.number)
    
def isSameCard(card1, card2):
    return card1.getNumber() == card2.getNumber() and card1.getSuit() == card2.getSuit()

def bubbleSort(Ain, N):
    for i in range(0,N):
        for j in range(N-1, i, -1):
            if Ain[j].getNumber() < Ain[j-1].getNumber():
                temp = Ain[j]
                Ain[j] = Ain[j-1]
                Ain[j-1] = temp

def selectionSort(Ain, N):
    for i in range(0,N):    # iは最小のカードが入る場所
        minj = i
        for j in range(i+1,N):   # jは最小候補カードのインデックス
            if Ain[j].getNumber() < Ain[minj].getNumber():
                minj = j
        temp = Ain[i]
        Ain[i] = Ain[minj]
        Ain[minj] = temp

def printCards(Ain, N):
    for i in range(N-1):
        print(str(Ain[i]) + " ", end="")
    print(str(Ain[N-1]))

N = int(input())
Ain = [Card(info) for info in input().split()]
Ab = [i for i in Ain]
As = [i for i in Ain]
bubbleSort(Ab, N)
selectionSort(As, N)
printCards(Ab, N)
print("Stable")
printCards(As, N)
for i in range(0,N):
    if not isSameCard(Ab[i], As[i]):
        print("Not stable")
        break
    elif i != N-1:
        continue
    print("Stable")

