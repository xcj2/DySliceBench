class Card:
    suit = ''
    value = 0

    def __init__(self, val):
        self.suit = val[0]
        self.value = int(val[1])

    def __lt__(self, rhv):
        return self.value < rhv.value

    def __le__(self, rhv):
        return self.value <= rhv.value

    def __eq__(self, rhv):
        return self.suit == rhv.suit and self.value == rhv.value

    def __ne__(self, rhv):
        return not (self == rhv)

    def __str__(self):
        return '%s%d'%(self.suit, self.value)

def merge(arr, length, left, mid, right):
#  n1 = mid - left
#  n2 = right - mid

    L = arr[left : mid]
    R = arr[mid : right]

    L.append(Card([' ', 2000000000]))
    R.append(Card([' ', 2000000000]))

    i, j = 0, 0
    for k in range(left, right):
        if (L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def merge_sort(arr, length, left, right):
    if (left + 1 < right):
        mid = (left + right)//2
        merge_sort(arr, length, left, mid)
        merge_sort(arr, length, mid, right)
        merge(arr, n, left, mid, right)

def partition(arr, left, right):
    x = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quick_sort(arr, length, left, right):
    if (left < right):
        q = partition(arr, left, right)
        quick_sort(arr, length, left, q - 1)
        quick_sort(arr, length, q + 1, right)

if __name__ == '__main__':
    n = int(input())

    arr1 = []
    arr2 = []

    for i in range(n):
        temp = input().split(' ')
        arr1.append(Card(temp))
        arr2.append(Card(temp))
    
    stable = True

    merge_sort(arr1, n, 0, n)
    quick_sort(arr2, n, 0, n - 1)

    for i in range(n):
        if (arr1[i].suit != arr2[i].suit):
            stable = False
            break
    if stable:
        print('Stable')
    else:
        print('Not stable')

    for i in arr2:
        print('%s %d'%(i.suit, i.value))
        
