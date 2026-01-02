def find(A):
    temp=[]
    ##split into R..RL..L
    left=1
    
    count1=0
    count2=0
    for i in range(len(A)):
        if left==1:
            if A[i]=="R":
                count1+=1
            else:
                
                count2=1
                left=0
        else:
            if A[i]=="L":
                count2+=1
            else:
                temp+=[(count1,count2)]
                count2=0
                count1=1
                left=1
    temp+=[(count1,count2)]
    return temp

def findout(x,y):
    org=x
    left=0
    right=0
    if x%2==0:
        left+=x//2
        right+=x//2
    else:
        left+=(x-1)//2+1
        right+=x-((x-1)//2+1)
    
    x=y
    if x%2==0:
        right+=x//2
        left+=x//2
    else:
        right+=(x-1)//2+1
        left+=x-((x-1)//2+1)
    
    return [0]*(org-1)+[left]+[right]+[0]*(y-1)


def findans(A):
    temp=find(A)
    ans=[]
    #print(temp)
    for (x,y) in temp:
        #print(findout(x,y))
        ans+=findout(x,y)
    return ans
s=input()
print(*findans(s))