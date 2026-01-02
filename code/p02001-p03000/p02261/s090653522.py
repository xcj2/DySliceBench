import copy
def inputInline():
    N = int(input())
    cards = input().split(" ")
    return cards

def selectionSort(list):
    cards=copy.deepcopy(list)
    n = len(cards)
    count = 0
    for i in range(n):
        min_j = i
        for j in range(i + 1, n):
            if int(cards[j][1]) < int(cards[min_j][1]):
                min_j = j
        if min_j != i:
            temp = cards[i]
            cards[i] = cards[min_j]
            cards[min_j] = temp
            count += 1
    return (" ".join(cards), count)

def bubbleSort(list):
    cards=copy.deepcopy(list)
    N = len(cards)
    count = 0
    flag = True
    while flag:
        flag = False
        for i in range(N - 1):
            if int(cards[i][1]) > int(cards[i + 1][1]):
                temp = cards[i]
                cards[i] = cards[i + 1]
                cards[i + 1] = temp
                flag = True
                count += 1
    return (" ".join(cards), count)
cards=inputInline()
sortedbubble=bubbleSort(cards)[0]
sortedselection=selectionSort(cards)[0]
print(sortedbubble)
print("Stable")
print(sortedselection)
if sortedbubble==sortedselection:
    print("Stable")
else:
    print("Not stable")