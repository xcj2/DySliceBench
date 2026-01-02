from bisect import bisect_left

def readinput():
    n=int(input())
    s=list(map(int,input().split()))
    q=int(input())
    t=list(map(int,input().split()))
    return n,s,q,t

def bisect_search(s,i):
    left=0
    right=len(s)
    while(left<right):
        middle=(left+right)//2
        #print(left,right)
        if(i==s[middle]):
            return True
        elif(s[middle]<i):
            left=middle+1
        else:
            right=middle
    return False

def main(n,s,q,t):
    c=0
    for i in t:
        res=bisect_search(s,i)
        if(res==True):
            c+=1
        
    return c

def find(a,x):
    i = bisect_left(a,x)
    if i != len(a) and a[i]==x:
        return True
    else:
        return False
     

def main2(n,s,q,t):
    c=0
    for i in t:
        if(find(s,i)==True):
            c+=1
    return c

if __name__=='__main__':
    n,s,q,t=readinput()
    ans=main2(n,s,q,t)
    print(ans)

