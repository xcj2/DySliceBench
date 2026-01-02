class Card:
    def __init__(self, suit='', num=''):
        self.suit = suit
        self.num = num
    def __str__(self):
        return "" + self.suit + self.num

def bubble_sort(list):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if list[j].num < list[j - 1].num:
                tmp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = tmp

def selection_sort(list):
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if list[j].num < list[mini].num:
                mini = j
        tmp = list[mini]
        list[mini] = list[i]
        list[i] = tmp

n = int(input())
inputs = [string for string in input().split(" ")]

cards = []
for i in range(n):
    cards.append(Card(inputs[i][0], inputs[i][1]))

selection_cards = cards.copy()

bubble_sort(cards)
selection_sort(selection_cards)

bubble_result = str(cards[0])
for i in range(1, n):
    bubble_result += " " + str(cards[i]);
print(bubble_result)
print("Stable")

selection_result = str(selection_cards[0])
stable_flag = (cards[0] == selection_cards[0])
for i in range(1, n):
    if cards[i] != selection_cards[i]:
        stable_flag = False
    selection_result += " " + str(selection_cards[i])
print(selection_result)
if stable_flag:
    print("Stable")
else:
    print("Not stable")
