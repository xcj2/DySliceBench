def cardnum(c):
    cc = list(c)
    return int(cc[1])

def cardlabel(c):
    cc = list(c)
    return cc[0]

def bubleSort(c, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if cardnum(c[j]) < cardnum(c[j-1]):
                (c[j], c[j-1]) = (c[j-1], c[j])
    return c

def selectionSort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if cardnum(c[j]) < cardnum(c[minj]):
                minj = j
        if minj != i:
            (c[i], c[minj]) = (c[minj], c[i])
    return c

def isStable(c1, c0):
    l0 = []
    l1 = []
    for i in range(1, 10):
        for j in range(len(c0)):
            if (cardnum(c0[j])==i):
                l0.append(cardlabel(c0[j]))
            if (cardnum(c1[j])==i):
                l1.append(cardlabel(c1[j]))
#    print(l0)
#    print(l1)
#    print(l0==l1)
    return l0 == l1
     

n = int(input())
cards = input().split()
c1 = cards.copy()
c1ret = bubleSort(c1, n)
print(' '.join(c1ret))
if (isStable(c1ret, cards)):
    print('Stable')
else:
    print('Not stable')

#print(c1, c1ret, cards)

c2 = cards.copy()
c2ret = selectionSort(c2, n)
print(' '.join(c2ret))
if (isStable(c2ret, cards)):
    print('Stable')
else:
    print('Not stable')

