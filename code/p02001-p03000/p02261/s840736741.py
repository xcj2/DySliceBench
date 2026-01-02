class Card:
    def __init__(self, mark, value):
        self.mark = mark
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value == other.value and self.mark == other.mark

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return self.mark + str(self.value)


def BubbleSort(arr):
    res = [Card(c.mark, c.value) for c in arr]
    swap_flg = True
    i = 0
    while swap_flg:
        swap_flg = False
        for j in range(len(res) - 1, i, -1):
            if (res[j] < res[j - 1]):
                res[j], res[j - 1] = res[j - 1], res[j]
                swap_flg = True
        i += 1
    return res


def SelectionSort(arr):
    res = [Card(c.mark, c.value) for c in arr]
    for i in range(0, len(res)):
        minj = i
        for j in range(i, N):
            if res[j] < res[minj]:
                minj = j
        if (i != minj):
            res[i], res[minj] = res[minj], res[i]
    return res


def isStable(in_arr, out_arr):
    stable_arr = BubbleSort(in_arr)
    return all(out_arr[i] == stable_arr[i] for i in range(0, len(out_arr)))


N = int(input())
arr = [Card(s[0], int(s[1])) for s in input().split()]
b_arr = BubbleSort(arr)
print(' '.join(map(str, b_arr)))
print('Stable' if isStable(arr, b_arr) else 'Not stable')
s_arr = SelectionSort(arr)
print(' '.join(map(str, s_arr)))
print('Stable' if isStable(arr, s_arr) else 'Not stable')

