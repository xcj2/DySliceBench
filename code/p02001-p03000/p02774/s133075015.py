from itertools import groupby

def sgn(num):
    if num<0:
        return -1
    elif num==0:
        return 0
    else:
        return 1


N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
a=0
b=0
c=0
B=[sgn(A[i]) for i in range(0,N)]
B=groupby(B)
for key,group in B:
    g=len(list(group))
    if key==-1:
        a=g
    elif key==0:
        b=g
    else:
        c=g
if a*c>=K:
    def condition(num):
        s=0
        t=a+b
        set=0
        while a+b+c-1>=t and a-1>=s:
            if A[s]*A[t]>num:
                t+=1
            else:
                set+=a+b+c-t
                s+=1
        if set>=K:
            return True
        else:
            return False
    start=-10**18
    end=-1
    while end-start>1:
        test=(start+end)//2
        if condition(test):
            end=test
        else:
            start=test
    if condition(start):
        print(start)
    else:
        print(end)
elif a*c+a*b+b*c+b*(b-1)//2>=K:
    print(0)
else:
    K-=a*c+a*b+b*c+b*(b-1)//2
    def condition(num):
        set=0
        s=a-1
        t=0
        while a-1>=t and s>=0:
            if A[s]*A[t]>num:
                t+=1
            else:
                set+=a-t
                if s>=t:
                    set-=1
                s-=1
        s=a+b
        t=a+b+c-1
        while t>=a+b and a+b+c-1>=s:
            if A[s]*A[t]>num:
                t-=1
            else:
                set+=t-a-b+1
                if t>=s:
                    set-=1
                s+=1
        if set>=2*K:
            return True
        else:
            return False
    start=1
    end=10**18
    while end-start>1:
        test=(end+start)//2
        if condition(test):
            end=test
        else:
            start=test
    if condition(start):
        print(start)
    else:
        print(end)
