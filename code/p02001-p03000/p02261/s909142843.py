import copy

def BubbleSort(card):
    card_b = []
    card_b = copy.deepcopy(card)
    for i in range(len(card_b)-1):
        j = len(card_b)-1
        while i+1 <= j:
            if list(card_b[j])[1] < list(card_b[j-1])[1]:
                w = card_b[j]
                card_b[j] = card_b[j-1]
                card_b[j-1] = w
            j -= 1
    return card_b

def SelectionSort(card):
    card_s = []
    card_s = copy.deepcopy(card)
    for i in range(len(card_s)-1):
        mini = i
        j = i
        while len(card_s)-1 >= j:
            if list(card_s[j])[1] < list(card_s[mini])[1]:
                mini = j
            j += 1
        w = card_s[i]
        card_s[i] = card_s[mini]
        card_s[mini] = w
    return card_s

def CardPrint(card):
    i = 0
    for c in card:
        if i != n-1:
            print("{} ".format(c), end="")
        elif i == n-1:
            print(c)
        i += 1


n = int(input())
card = input().split()

r1 = []
r1 = BubbleSort(card)
CardPrint(r1)
print("Stable")

r2 = []
r2 = SelectionSort(card)
CardPrint(r2)
if r1 == r2:
    print("Stable")
else:
    print("Not stable")

