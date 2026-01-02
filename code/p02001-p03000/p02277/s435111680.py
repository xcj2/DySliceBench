class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


def merge(a, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    l = a[left:left+n1]
    r = a[mid:mid+n2]
    l.append(Card('X', float('inf')))
    r.append(Card('X', float('inf')))
    i = 0
    j = 0
    for k in range(left, right):
        if l[i].value <= r[j].value:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1


def mergeSort(a, left, right):
    if left+1 < right:
        mid = (left+right) // 2
        mergeSort(a, left, mid)
        mergeSort(a, mid, right)
        merge(a, left, mid, right)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j].value <= x.value:
            i += 1
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    tmp = a[r]
    a[r] = a[i+1]
    a[i+1] = tmp
    return i + 1


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q-1)
        quickSort(a, q+1, r)


n = int(input())
a = []
b = []
for i in range(n):
    tmp = input().split()
    a.append(Card(tmp[0], int(tmp[1])))
    b.append(Card(tmp[0], int(tmp[1])))

mergeSort(a, 0, n)
quickSort(b, 0, n-1)

is_stable = True
for i in range(n):
    if a[i].suit != b[i].suit:
        is_stable = False
        break

if is_stable:
    print('Stable')
else:
    print('Not stable')

for v in b:
    print('%s %d' % (v.suit, v.value))
