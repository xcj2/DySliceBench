from collections import namedtuple
from operator import itemgetter, attrgetter

def bubble_sort(a):
    a = a[:]
    n = len(a)

    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j].value < a[j - 1].value:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def selection_sort(a):
    a = a[:]
    n = len(a)

    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j].value < a[minj].value:
                minj = j
        a[i], a[minj] = a[minj], a[i]

    return a

class Card(namedtuple('Card', ['suit', 'value'])):
    def __str__(self):
        return '{0}{1}'.format(self.suit, self.value)

parser = lambda s: Card(s[0], int(s[1:]))

n = int(input())
a = list(map(parser, input().split()))

stable_sorted = sorted(a, key = attrgetter('value'))
bubble_sorted = bubble_sort(a)
selection_sorted = selection_sort(a)

print(' '.join(list(map(str, bubble_sorted))))
if stable_sorted == bubble_sorted:
    print('Stable')
else:
    print('Not stable')

print(' '.join(list(map(str, selection_sorted))))
if stable_sorted == selection_sorted:
    print('Stable')
else:
    print('Not stable')