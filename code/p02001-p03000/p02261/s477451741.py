class card:
    """
    suit: S, H, C, D
    number: 1~10
    """
    def __init__(self, card_input):
        self.suit = card_input[:1]
        self.number = int(card_input[1:])
    
    def __str__(self):
        return self.suit + str(self.number)


def print_list(a):
    out = ''
    for ai in a:
        out += str(ai) + ' '
    else:
        out = out[:-1]
    print(out)

def bubble_sort(a, n):
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if a[j].number < a[j - 1].number:
                tmp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tmp
    return a
                
def selection_sort(a, n):
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if a[j].number < a[minj].number:
                minj = j
        tmp = a[i]
        a[i] = a[minj]
        a[minj] = tmp
    return a

n = int(input())
input_cards = input().split(' ')
cards = []
for in_card in input_cards:
    cards.append(card(in_card))

bubble = bubble_sort(cards[:], n)
print_list(bubble)
print("Stable")

selection = selection_sort(cards[:], n)
print_list(selection)
if bubble == selection:
    print("Stable")
else:
    print("Not stable")
