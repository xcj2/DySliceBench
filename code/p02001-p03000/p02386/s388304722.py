def East(a,b,c,d,e,f):
    return [d, b, a, f, e, c]
def West(a,b,c,d,e,f):
    return [c, b, f, a, e, d]
def South(a,b,c,d,e,f):
    return [e, a, c, d, f, b]
def North(a,b,c,d,e,f):
    return [b, f, c, d, a, e]
def Rot(a,b,c,d,e,f):
    return [a,d,b,e,c,f]



def Judge(change, change_after):
    flag=0
    for idx in range(0, 5):
        change=South(*change)
        #print(change)
        if change==change_after:
            flag=flag+1
        for idx2 in range(0,4):
            change=Rot(*change)
            #print(change)
            if change==change_after:
               flag=1+flag
               
    for idx in range(0, 5):
        change=West(*change)
        #print(change)
        if change==change_after:
            flag=flag+1
        for idx2 in range(0,4):
            change=Rot(*change)
            #print(change)
            if change==change_after:
               flag=1+flag
    return flag
    
n=int(input())
matrix=[]
for i in range(0, n):
    change=list( map(int,input().split()))
    matrix.append(change)
    #change_after=list( map(int,input().split()))

judge_number=0
for i in range(0, n-1):
    change=matrix[i]
    for j in range(i+1, n):
        change_after=matrix[j]
        judge_number=Judge(change, change_after)+judge_number
       

if judge_number==0:
    print("Yes")
else:
    print("No")

