
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + ' ' + str(self.value)


""" merge_sort """

def merge(A, n, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]

    L.append(Card('None', 2000000000))  # これをしないとマージするとき、最後の１回でリスト外アクセスでエラー。
    R.append(Card('None', 2000000000))

    # global count
    i, j = 0, 0

    # print('left, mid, right')
    # print(left, mid, right)

    for k in range(left, right, 1):
        # count += 1
        # print('i, j, k')
        # print(i, j, k)

        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

        # print('loop end')


def merge_sort(A, n, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(A, n, left, mid)
        merge_sort(A, n, mid, right)
        merge(A, n, left, mid, right)


""" quick_sort """

def partition(A, n, p, r):
    x = A[r].value
    i = p - 1

    for j in range(p, r):
        if A[j].value <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quick_sort(A, n, p, r):
    if p < r:
        q = partition(A, n, p, r)
        quick_sort(A, n, p, q-1)
        quick_sort(A, n, q+1, r)


N = int(input())
A = []
for i in range(N):
    suit, value = input().split()
    value = int(value)
    A.append(Card(suit, value))
B = list(A)

quick_sort(A, N, 0, N-1)
merge_sort(B, N, 0, N)

stable = True
for i in range(N):
    if A[i] != B[i]:
        stable = False

if stable is True:
    print('Stable')
else:
    print('Not stable')

for a in A:
    print(a)

# for b in B:
#     print(b)

