def appendnum(lis) :
    for i in range(1,14):
        lis.append(i)

def removenum(lis,num) :
    lis.remove(num)
    
def shownum(lis,S):
    for s in lis:
        print(S,s)
        
Slist = list()
Hlist = list()
Clist = list()
Dlist = list()

appendnum(Slist)
appendnum(Hlist)
appendnum(Clist)
appendnum(Dlist)

n = int(input())

for i in range(n):
    suit, num = input().split()
    suit = str(suit)
    num = int(num)
    if suit == "S":
        removenum(Slist,num)
    elif suit == "H":
        removenum(Hlist,num)
    elif suit == "C" :
        removenum(Clist,num)
    elif suit == "D" :
        removenum(Dlist,num)
        
shownum(Slist,"S")
shownum(Hlist,"H")
shownum(Clist,"C")
shownum(Dlist,"D")

