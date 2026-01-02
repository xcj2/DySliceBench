def partition(A,p,r):#A[p]〜A[r-1]までのリストをpartitionする
    x=A[r-1][1]
    i=p-1
    for j in range(p,r-1):
        if(A[j][1] <= x):
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r-1]=A[r-1],A[i+1]
    return i+1
    

def quick_sort(A,p,r):
    if( p < r-1 ):
        q=partition(A,p,r)
        quick_sort(A,p,q)
        quick_sort(A,q+1,r)

        


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





n=int(input())
original_cards=[]
for loop in range(n):
    original_cards.append(list(input().split()))
for card in original_cards:
    card[1]=int(card[1])

sorted_cards=[card for card in original_cards]
quick_sort(sorted_cards,0,n)

if(stability_judge(sorted_cards,original_cards)):
    print("Stable")
else:
    print("Not stable")



for card in sorted_cards:
    card[1]=str(card[1])
    print(" ".join(card))
