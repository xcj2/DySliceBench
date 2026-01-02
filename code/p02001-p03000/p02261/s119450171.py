class Selection_sort:
    def __init__(self):
        self.swap_num=0
    
    def sort(self,data):
        for i in range(len(data)):
            mini=i
            for j in range(i+1,len(data)):
                if(data[j][1] < data[mini][1]):
                    mini=j
            if(mini!=i):
                data[i],data[mini]=data[mini],data[i]
                self.swap_num+=1


class Bubble_sort:
    def __init__(self):
        self.swap_num=0
    
    def sort(self,list):
        for i in range(len(list)):
            for j in range(i+1,len(list))[::-1]:
                if(list[j][1] < list[j-1][1]):
                    list[j],list[j-1]=list[j-1],list[j]
                    self.swap_num+=1


def stability_judge(sorted,original):
    n=len(sorted)
    j=-1
    x=sorted[0][1]
    for i in range(n):
        if(x!=sorted[i][1]):
            x=sorted[i][1]
            j=-1
        
        while(1):
            j+=1
            if(x==original[j][1]):
                if(sorted[i][0]!=original[j][0]):
                    return 0
                else:
                    break
    return 1


def cards_print(cards):
    newcards=[]
    for card in cards:
        card[1]=str(card[1])
    newcards=["".join(card) for card in cards]    
    print(" ".join(newcards))




n=int(input())
cards=[list(str) for str in input().split()]
for card in cards:
    card[1]=int(card[1])

b_cards=[i for i in cards]
s_cards=[i for i in cards]


bubble_sort=Bubble_sort()
bubble_sort.sort(b_cards)
#x=stability_judge(b_cards,cards)
cards_print(b_cards)

if(stability_judge(b_cards,cards)):
    print("Stable")
else:
    print("Not stable")



selection_sort=Selection_sort()
selection_sort.sort(s_cards)
cards_print(s_cards)
if(stability_judge(s_cards,cards)):
    print("Stable")
else:
    print("Not stable")
