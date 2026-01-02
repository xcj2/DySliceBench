# Stable Sort

length = int(input())
cards = input().rstrip().split()
cards1 = [card for card in cards]
cards2 = [card for card in cards]

def value(n):
    number = n[1:]
    return int(number)

def char(cards):
    charSets = [[] for i in range(10)]
    for i in range(length):
        char = cards[i][:1]
        val = value(cards[i])
        # print('絵柄: ' + char + ', 数字: ' + str(val))
        charSets[val].append(char)
    return charSets

def bubble(cards):
    for i in range(length):
        j = length - 1
        while j > i:
            if value(cards[j]) < value(cards[j - 1]):
                cards[j], cards[j - 1] = cards[j - 1], cards[j]
            j -= 1
    return cards

def selection(cards):
    # count = 0
    for i in range(length):
        minj = i
        for j in range(i, length):
            if value(cards[j]) < value(cards[minj]):
                minj = j
        #if minj != i:
            # count += 1
        cards[i], cards[minj] = cards[minj], cards[i]
    return cards

def stable(cards1, cards2):
    if char(cards1) == char(cards2):
        return 'Stable'
    else:
        return 'Not stable'

c = cards
b = bubble(cards1)
s = selection(cards2)

print(' '.join(b))
print(stable(c, b))
print(' '.join(s))
print(stable(c, s))

