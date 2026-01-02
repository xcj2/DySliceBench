class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
def selection(ls):
    for i in range(len(ls)):
        minj = i
        
        for j in range(i, len(ls)):
            if ls[j].value < ls[minj].value:
                minj = j
        ls[i], ls[minj] = ls[minj], ls[i]

def bubblesort(ls):
    for i in range(1, len(ls)):
        for j in reversed(range(i, len(ls))):
            if ls[j].value < ls[j-1].value:
                ls[j], ls[j-1] = ls[j-1], ls[j]

def isStable(ls1, ls2):
    if ls1 == ls2:
        print("Stable")
    else:
        print("Not stable")

def printcards(cards):
    for x in range(len(cards)):
        if x == len(cards) - 1:
            print(cards[x].suit + cards[x].value)
        else:
            print(cards[x].suit + cards[x].value, ' ', sep='', end='')

def main():
    N = int(input().rstrip())

    cards = []
    for card in list(input().split(' ')):
        cards.append(Card(card[0], card[1]))

    a = [x for x in cards]
    b = [x for x in cards]
    

    bubblesort(a)
    selection(b)
    
    printcards(a)
    print("Stable")

    printcards(b)
    isStable(a,b)
    
if __name__ == '__main__':
    main()