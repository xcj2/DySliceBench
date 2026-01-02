# 比较冒泡排序和选择排序

def bubble_sort(arr):
    no_swap = True
    #swap_cnt = 0
    for i in range(len(arr), 0, -1):
        if not no_swap:
            break
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                #swap_cnt += 1
            no_swap = True
    #return swap_cnt

def selection_sort(arr):
    #swap_cnt = 0
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            #swap_cnt += 1
    #return swap_cnt

# n^4 method
def is_stable(raw, sort_):
    N = len(raw)
    for i in range(N):
        for j in range(i + 1, N):
            for m in range(N):
                for n in range(m + 1, N):
                    if (raw[i].value == raw[j].value) and (raw[i] == sort_[n]) and (raw[j] == sort_[m]):
                        return 'Not stable'
    return 'Stable'

class Card:
    suit = ''
    value = 0

    def __init__(self, val):
        self.suit = val[0]
        self.value = int(val[1])

    def __lt__(self, rhv):
        return self.value < rhv.value

    def __eq__(self, rhv):
        return self.suit == rhv.suit and self.value == rhv.value

    def __ne__(self, rhv):
        return not (self == rhv)

    def __str__(self):
        return '%s%d'%(self.suit, self.value)

if __name__ == '__main__':
    N = int(input())
    raw = list(map(Card, input().split()))
    arr1 = []
    arr2 = []
    for i in raw:
        arr1.append(i)
        arr2.append(i)
    bubble_sort(arr1)
    result = is_stable(raw, arr1)
    print(' '.join(map(str, arr1)))
    # print('Stable')
    print(result)
    selection_sort(arr2)
    print(' '.join(map(str, arr2)))
    result = is_stable(raw, arr2)
    print(result)
    # for i in range(len(arr1)):
    #     if arr1[i] != arr2[i]:
    #         print('Not stable')
    #         break
    #     if i == len(arr1) - 1:
    #         print('Stable')

