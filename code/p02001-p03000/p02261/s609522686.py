# Stable sort
class Card:
    def __init__(self, c):
        self.suit = c[0]
        self.value = int(c[1])
def toi(c):
    return c.value
def toStr(c):
    return c.suit + str(c.value)
def bubble_sort(C,N):
    for i in range(0, N):
        for j in range(N-1,i,-1):
            if C[j].value < C[j-1].value:
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
    return (C,True)
def selection_sort(C,N):
    st = True
    for i in range(0,N):
        minj = i
        for j in range(i,N):
            # ????????§??????????´??????????????????°??????????????§?????????????????????????????????
            if C[j].value < C[minj].value:
                minj = j
        if not i == minj:
            if (list(map(toi, C[i:]))).count(C[i].value) > 1: st = False
            tmp = C[i]
            C[i] = C[minj]
            C[minj] = tmp
    return (C, st)
N = int(input())
C = [Card(i) for i in input().split(' ')]
C1, isstable1 = bubble_sort(C[:],N)
print(' '.join(list(map(toStr, C1))))
if isstable1: print('Stable')
else: print('Not stable')
C2, isstable2 = selection_sort(C[:],N)
print(' '.join(list(map(toStr, C2))))
if isstable2: print('Stable')
else: print('Not stable')
