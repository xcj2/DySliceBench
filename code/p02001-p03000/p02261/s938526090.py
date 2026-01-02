import copy

def show(C):
    N=len(C)
    for i in range(N):
        if i<N-1:
            print(C[i][0]+str(C[i][1]),end=' ')
        else:
            print(C[i][0]+str(C[i][1]))
    
def BubbleSort(C,N):
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if int(C[j][1])<int(C[j-1][1]):
                C[j],C[j-1]=C[j-1],C[j]
    return C

def SelectionSort(C,N):
    for i in range(N):
        minj=i
        for j in range(i,N):
            if int(C[minj][1])>int(C[j][1]):
                minj=j
        C[i],C[minj]=C[minj],C[i]
    return C

def compare(C1,C2):
    for i in range(1,10):
        l1=[]
        for c in C1:
            if int(c[1])==i:
                l1.append(c)
        l2=[]
        for c in C2:
            if int(c[1])==i:
                l2.append(c)
        for j in range(min(len(l1),len(l2))):
            if l1[j][0]!=l2[j][0]:
                return False
    return True
   
N=int(input())
l=list(input().split())
deck=[]
for c in l:
    deck.append((c[0],c[1]))

deck1=copy.copy(deck)
deck2=copy.copy(deck)

deck1=BubbleSort(deck1,N)
deck2=SelectionSort(deck2,N)

show(deck1)
compare(deck,deck1)
print('Stable' if compare(deck,deck1) else 'Not stable')
show(deck2)
print('Stable' if compare(deck,deck2) else 'Not stable')
