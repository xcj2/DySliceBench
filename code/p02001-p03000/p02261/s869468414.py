import copy
N=int(input())
c1=list(input().split())
c2=copy.deepcopy(c1)
c3=copy.deepcopy(c1)
def bubble(card):
    for i in range(N):
        for j in [N-x for x in range(1,N-i)]:
            if int(card[j][1]) < int(card[j-1][1]):
                s= card[j]
                card[j]=card[j-1]
                card[j-1]=s
    return card
def selection(card):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(card[j][1]) < int(card[minj][1]):
                minj = j
        s = card[i]
        card[i]=card[minj]
        card[minj]=s
    return card
def stable(card):
    j=0
    for i in range(N-1):
        if int(card[i][1]) == int(card[i+1][1]):
            if c3.index(card[i]) > c3.index(card[i+1]):
                j=1
                break
    if j == 0:
        return 'Stable'
    else:
        return 'Not stable' 
print(*bubble(c1))
print(stable(bubble(c1)))
print(*selection(c2))
print(stable(selection(c2)))
