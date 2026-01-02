def readinput():
    n=int(input())
    cards=[]
    nums=set()
    for _ in range(n):
        m,nn=input().split()
        nn=int(nn)
        cards.append((m,nn))
        nums.add(nn)
    return n,cards, nums

def partition(cards,p,r):
    #print('before:',end='');print(cards[p:r+1])
    x=cards[r][1]
    i=p-1
    for j in range(p,r):
        if (cards[j][1] <= x):
            i+=1
            cards[j],cards[i]=cards[i],cards[j]
            #print(cards[p:r+1])
    cards[i+1],cards[r]=cards[r],cards[i+1]
    #print('after:',end='');print(cards[p:r+1])
    return i+1

def quickSort(cards,p,r):
    if (p<r):
        q=partition(cards,p,r)
        quickSort(cards,p,q-1)
        quickSort(cards,q+1,r)

def getMarks(cards,n):
    marks=[]
    for card in cards:
        if(card[1]==n):
            marks.append(card[0])
    return marks

def isStable(cards0, cards1, nums):
    for n in nums:
        marks0=getMarks(cards0,n)
        marks1=getMarks(cards1,n)
        if(marks0!=marks1):
            return False
    return True

def main(n,cards,nums):
    original = cards.copy()
    quickSort(cards,0,n-1)
    ans=isStable(original, cards, nums)
    if(ans==True):
        print('Stable')
    else:
        print('Not stable')
    for card in cards:
        print(card[0]+' '+str(card[1]))
    return

if __name__=='__main__':
    n,cards,nums=readinput()
    main(n,cards,nums)

