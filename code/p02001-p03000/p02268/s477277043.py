def inputting():
    n=int(input())
    S=sorted(map(int,input().split()))
    q=int(input())
    T=list(map(int,input().split()))
    return n,S,q,T


def binarysearch( s, e, S, t):
    if s>=e:
        return 0
    elif S[(s+e)//2]==t:
        return 1
    elif S[(s+e)//2]>t:
        return binarysearch( s, (s+e)//2, S, t)
    elif S[(s+e)//2]<t:
        return binarysearch((s+e)//2+1, e, S, t)

    
def main():
    n,S,q,T=inputting()
    count=0
    for t in T:
        flag=binarysearch(0,n,S,t)
        if flag==1:
            count+=1
    print(count)

if __name__=='__main__':
    main()

