class Card:
    def __init__(self, num, suit, input_index):
        self.num = num
        self.suit = suit
        self.input_index = input_index


def partition(A, p, r):
    x = A[r - 1].num
    i = p - 1
    for j in range(p, r - 1):
        if A[j].num <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r-1:
        index = partition(A, p, r)
        quick_sort(A, p, index)
        quick_sort(A, index, r)


n = int(input())
li = [None] * n
for i in range(n):
    temp_list = list(map(str, input().split()))
    li[i] = Card(int(temp_list[1]), temp_list[0], i)

quick_sort(li, 0, n)

for i in range(n):
    if i < n - 1 and li[i].num == li[i + 1].num and li[i].input_index > li[i + 1].input_index:
        print('Not stable')
        break
    if i == n - 1:
        print('Stable')

for card in li:
    print(card.suit + ' {}'.format(card.num))

