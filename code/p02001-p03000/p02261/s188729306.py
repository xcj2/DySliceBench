class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def getCard(self):
        return self.suit + str(self.value)

def SelectionSort(C):
    A=C
    # sort
    for i in range(len(A)):
        mini=i
        for j in range(i,len(A)):
            if A[j].value<A[mini].value:
                mini=j
        if mini!=i:
            tmp=A[i]
            A[i]=A[mini]
            A[mini]=tmp
    return A

def BubbleSort(C):
    A=C
    for i in range(len(A)):
        for j in reversed(range(i+1,len(A))):
            if A[j].value < A[j-1].value:
                tmp=A[j]
                A[j]=A[j-1]
                A[j-1]=tmp
    return A

def getCardString(A):
    maplist=[]
    for a in A:
        maplist.append(a.getCard())
    return ' '.join(maplist)

n=int(input())
cardsA=[]
cardsB=[]
for data in input().split():
    charList=list(data)
    cardsA.append(Card(charList[0],int(charList[1])))
    cardsB.append(Card(charList[0],int(charList[1])))
bubble=getCardString(BubbleSort(cardsA))
select=getCardString(SelectionSort(cardsB))
print(bubble)
print('Stable')
print(select)
print('Stable' if select==bubble else 'Not stable')



