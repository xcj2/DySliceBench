flag=[0 for i in range(64)]

def Test(flag,i):
    print(flag[i])

def Set(flag,i):
    flag[i]=1
    return flag

def Clear(flag,i):
    flag[i]=0
    return flag

def Flip(flag,i):
    if flag[i]==0:
        flag[i]=1
    else:
        flag[i]=0
    return flag

def All(flag):
    if all(flag)==True:
        print(1)
    else:
        print(0)

def Any(flag):
    if any(flag)==True:
        print(1)
    else:
        print(0)

def none(flag):
    if not any(flag)==True:
        print(1)
    else:
        print(0)

def Val(flag):
    a=''.join(map(str,flag[::-1]))
    print(int(a,2))

q=int(input())
for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==0:
        Test(flag,query[1])
    elif query[0]==1:
        flag=Set(flag,query[1])
    elif query[0]==2:
        flag=Clear(flag,query[1])
    elif query[0]==3:
        flag=Flip(flag,query[1])
    elif query[0]==4:
        All(flag)
    elif query[0]==5:
        Any(flag)
    elif query[0]==6:
        none(flag)
    elif query[0]==7:
        print(flag.count(1))
    else:
        Val(flag)

