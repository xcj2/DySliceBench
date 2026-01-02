import copy

class card:
    def __init__(self, s):
        self.value = int(s[1:])
        self.mark = s[0]
        self.s = s
    
    def __repr__(self):
        return self.s
        
def isstable(Cin, Cout, n):
    for i in range(n):
        for j in range(i+1, n):
            for a in range(n):
                for b in range(a+1, n):
                    if Cin[i].value==Cin[j].value and Cout[a].s==Cin[j].s and Cout[b].s == Cin[i].s:
                        return False
    return True
    
def BubbleSort(C, N):
    Cin = copy.copy(C)
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j].value < C[j-1].value:
                C[j], C[j-1] = C[j-1], C[j]
    print(*C)

    if isstable(Cin, C, N):
        print('Stable')
    else:
        print('Not stable')

def SelectionSort(C,N):
    Cin = copy.copy(C)
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        if minj!=i:
            C[i], C[minj] = C[minj], C[i]

    print(*C)
    if isstable(Cin, C, N):
        print('Stable')
    else:
        print('Not stable')

N = int(input())
C = list(map(card, input().split()))

#N = 5
#C = list(map(card, ['H4', 'C9', 'S4', 'D2', 'C3']))
BubbleSort(copy.copy(C), N)
SelectionSort(copy.copy(C), N)


