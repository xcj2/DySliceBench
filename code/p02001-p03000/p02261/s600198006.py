class Card():
    def __init__(self, card):
        self.card = card
        self.mark = card[0]
        self.number = card[1]
        
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.number < other.number
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.mark == other.mark and self.number == other.number
        
    def __repr__(self):
        return '{}{}'.format(self.mark, self.number)

    def ls_sort(self):
        return


def BubbleSort(target):
    ls = target.copy()
    flag = 1
    while flag:
        flag = 0
        for i in range(len(ls)-1, 0, -1):
            if ls[i] < ls[i-1]:
                ls[i], ls[i-1] = ls[i-1], ls[i]
                flag = 1
    print(' '.join(map(str, ls)))
    return sorted(ls)


def SelectSort(target):
    ls = target.copy()
    for i in range(len(ls)):
        minj = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[minj]:
                minj = j
        if ls[i] != ls[minj]:
            ls[i], ls[minj] = ls[minj], ls[i]
    
    print(' '.join(map(str, ls)))
    return sorted(ls)

def judge(original, sorted_list):
    if original == sorted_list:
        print('Stable')
    else:
        print('Not stable')


_ = int(input())
l2 =  [Card(i) for i in input().split()]
l2_sort = sorted(l2)

bubble = BubbleSort(l2)
judge(l2_sort, bubble)

select = SelectSort(l2)
judge(l2_sort, select)
