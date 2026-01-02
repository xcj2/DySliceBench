import copy
def bubblesort(card,maisu):
    for i in range(maisu):
        for j in reversed(range(i+1,maisu)):
            if card[j][1]<card[j-1][1]:
                card[j-1],card[j]=card[j],card[j-1]

def selectionsort(card,maisu):
    for i in range(maisu):
        mini=i
        for j in range(i,maisu):
            if card[j][1]<card[mini][1]:
                mini=j
        card[i],card[mini]=card[mini],card[i]

def output(card,maisu):
    joutai="Stable"
    for i in range(maisu):
        if i>0:
            print(" ",end="")
        print(card[i][0]+card[i][1],end="")
        if i<=maisu-2:
            if card[i][1]==card[i+1][1] and card[i][2]>card[i+1][2]:
                joutai="Not stable"
    print()
    print(joutai)
    
maisu=int(input())
card=list(map(str,input().split()))
for i in range(maisu):
    a=[]
    for j in card[i]:
        a.append(j)
    a.append(i)
    card[i]=a
    
card_bubble=copy.deepcopy(card)
card_selection=copy.deepcopy(card)

bubblesort(card_bubble,maisu)
output(card_bubble,maisu)

selectionsort(card_selection,maisu)
output(card_selection,maisu)

