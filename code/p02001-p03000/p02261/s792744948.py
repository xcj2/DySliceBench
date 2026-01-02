class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + str(self.value)

def ChkIfStable(c1, c2):
    for v in range(1,10):
        a1=[]
        for k1 in c1:
            if k1.value == v: a1.append(k1.suit)
        a2=[]
        for k2 in c2:
            if k2.value == v: a2.append(k2.suit)
        if a1!=a2:
            print('Not stable')
            return
    print('Stable')

def BubbleSort(C):
    for i in range(0, len(C)):
        for j in range(len(C)-1,i,-1):
            if C[j].value < C[j-1].value:
                 C[j], C[j-1] = C[j-1], C[j]
    return C

def SelectionSort(C):
    for i in range(len(C)):
        mini = i
        for j in range(i, len(C)):
            if C[j].value < C[mini].value:
                mini = j
        C[i], C[mini] = C[mini], C[i]
    return C

cc = []
input()
for c in input().split():
    cc.append(Card(c[0], int(c[1])))

bs=BubbleSort(cc[:])
print(' '.join(map(str,bs)))
ChkIfStable(cc, bs)
ss=SelectionSort(cc[:])
print(' '.join(map(str,ss)))
ChkIfStable(cc, ss)
