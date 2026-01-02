def main():
    cardList = makeCardList()
    n = int(input())
    for a in range(n):
        card = input()
        cardList[cardToIndex(card)] = ''
    for x in range(len(cardList)):
        if cardList[x]:
            print(cardList[x])

def makeCardList():
    cardList = []
    suits = ['S', 'H', 'C', 'D']
    for s in range(4):
        for r in range(13):
            cardList.append(suits[s] + ' ' + str(r+1))
    return cardList

def cardToIndex(c):
    dict = {'S':0, 'H':1, 'C':2, 'D':3}
    return (dict[c[0]] * 13 + int(c[2:]) - 1)

main()
