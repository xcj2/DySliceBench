class Card(object):
    def __init__(self, card):
        self.suit = card[:1]
        self.value = int(card[1:])
    
    def __str__(self):
        return self.suit + str(self.value)

def is_stable(bs, ss):
    if bs == ss:
        return 'Stable'
    else:
        return 'Not stable'

def bubble_sort(c, n):
    c = c.split()
    c = [Card(card) for card in c]
    for i in range(n-1):
        for j in range(n-1):
            if c[j].value > c[j+1].value:
                c[j], c[j+1] = c[j+1], c[j]
    return c

def selection_sort(c, n):
    c = c.split()
    c = [Card(card) for card in c]
    for i in range(n):
        mink = i
        for v in range(i, n):
            if c[v].value < c[mink].value:
                mink = v
        if mink != i:
            c[i], c[mink] = c[mink], c[i]
    return c

n = input()
nums = input()

bs = bubble_sort(nums, int(n))
bs_str = [str(card) for card in bs]
print(' '.join(bs_str))
print('Stable')

ss = selection_sort(nums, int(n))
ss_str = [str(card) for card in ss]
print(' '.join(ss_str))
print(is_stable(bs_str, ss_str))
