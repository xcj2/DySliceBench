from collections import namedtuple
Card = namedtuple('Card', 'suit value')

def BubbleSort(C):
    for i in range(len(C)):
        for j in range(len(C)-1,i,-1):
            if C[j].value < C[j-1].value:
                C[j],C[j-1] = C[j-1],C[j]

def SelectionSort(C):
    for i in range(len(C)):
        mini = i
        for j in range(i,len(C)):
            if C[j].value < C[mini].value:
                mini = j
        C[i],C[mini] = C[mini],C[i]

def checkStable(C0, C1):
    result = True
    for i in range(1,10):
        f0 = [x.suit for x in list(filter(lambda c: c.value==i,C0))]
        f1 = [x.suit for x in list(filter(lambda c: c.value==i,C1))]
        if f0!=f1:
            result = False
    return result

if __name__=='__main__':
    N = int(input()) 
    Co = list(map(lambda X: Card(X[0],int(X[1])), map(list, input().split())))
    Cb,Cs = [Co[:] for _ in range(2)]
    for C, Sort in zip([Cb,Cs], [BubbleSort, SelectionSort]):
        Sort(C)
        print(*["".join([X.suit,str(X.value)]) for X in C])
        print("Stable" if checkStable(Co,C) else "Not stable")