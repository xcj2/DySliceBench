import copy

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

'''
def insertionsort(a,n,g):
    for i in range(g,n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j - g
            cnt += 1
        a[j+g] = v
    return a
'''

def shellsort(a,n):
    cnt = 0
    def insertionsort(a,n,g,cnt):
        for i in range(g,n):
            v = a[i]
            j = i-g
            while j>= 0 and a[j] > v:
                a[j+g] = a[j]
                j = j-g
                cnt += 1
            a[j+g] = v
        return a, cnt

    g = [1]
    while g[-1]*3 + 1 < n:
        g.append(g[-1]*3+1)
    g = g[::-1]
    for i,x in enumerate(g):
        a, cnt = insertionsort(a,n,x,cnt)
    return a, len(g), g, cnt


def bubblesort(n,a):
    flag = 1
    while flag:
        flag = False
        for i in reversed(range(1,n)):
            if a[i-1].value > a[i].value:
                a[i], a[i-1] = a[i-1], a[i]
                flag = True
    return a

def selectionsort(n,a):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j].value < a[minj].value:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    return a

def is_stable(before, after):
    n = 9
    lb = [[] for _ in range(n)]
    la = [[] for _ in range(n)]
    for i in range(len(before)):
        lb[before[i].value-1].append(before[i].suit)
        la[after[i].value-1].append(after[i].suit)
    if la == lb:
        print('Stable')
    else:
        print('Not stable')


if __name__ == '__main__':
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a, m, g, cnt = shellsort(a,n)
    print(m)
    print(' '.join(map(str, g)))
    print(cnt)
    for x in a:
        print(x)

    






