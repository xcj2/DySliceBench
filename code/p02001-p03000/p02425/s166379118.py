def ope_all(l):
    cnt=[1 if sum(l)==64 else 0]
    return print(*cnt)

def ope_any(l):
    cnt=[0 if sum(l)==0 else 1]
    return print(*cnt)

def ope_none(l):
         cnt=[1 if sum(l)==0 else 0]
         return print(*cnt)    
         
li=[0]*64
n=int(input())
ope=[input().split() for i in range(n)]
ope =[[int(j) for j in ope[i]] for i in range(len(ope))]
for i in range(n):
    if ope[i][0]==0:
        n=[1 if li[ope[i][1]]==1 else 0]
        print(*n)
    elif ope[i][0]==1:
        li[ope[i][1]]=1
    elif ope[i][0]==2:
         li[ope[i][1]]=0       
    elif ope[i][0]==3:
        if li[ope[i][1]]==1:
            li[ope[i][1]]=0
        else:
            li[ope[i][1]]=1
    elif ope[i][0]==4:
        ope_all(li)
    elif ope[i][0]==5:
        ope_any(li)
    elif ope[i][0]==6:
         ope_none(li)
    elif ope[i][0]==7:
         print(li.count(1))
    else:
        int_li ="".join(map(str, li))
        int_li ="".join(list(reversed(int_li)))
        print(int(int_li,2))
         
