import copy

n = int(input())
cards = input().split()
#print(cards)
def bubble_sort(cards, n):
    c = copy.copy(cards)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if int(c[j][1]) < int(c[j-1][1]):
                tmp = c[j]
                c[j] = c[j-1]
                c[j-1] = tmp
    return c
    
bubble = bubble_sort(cards, n)
#print(cards)
#print(bubble)
print(' '.join(bubble))

def is_stable(o, s):
    for i in range(n - 1):
        if int(s[i][1]) == int(s[i+1][1]):
            if o.index(s[i]) > o.index(s[i+1]):
                return False
    return  True

if is_stable(cards, bubble):
    print('Stable')
else:
    print('Not stable')


def selection_sort(cards, n):
    c = copy.copy(cards)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(c[j][1]) < int(c[minj][1]):
                minj = j
        tmp = c[i]
        c[i] = c[minj]
        c[minj] = tmp
    return c

selection = selection_sort(cards, n)
print(' '.join(selection))

if is_stable(cards, selection):
    print('Stable')
else:
    print('Not stable')

