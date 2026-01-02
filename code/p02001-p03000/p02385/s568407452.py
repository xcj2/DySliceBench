change=list( map(int,input().split()))
change_after=list( map(int,input().split()))

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



flag=0
for idx in range(0, 5):
    change=South(*change)
    if change==change_after:
        flag=flag+1
    for idx2 in range(0,4):
        change=Rot(*change)
        if change==change_after:
           flag=1+flag
           
for idx in range(0, 5):
    change=West(*change)
    if change==change_after:
        flag=flag+1
    for idx2 in range(0,4):
        change=Rot(*change)
        if change==change_after:
           flag=1+flag
if flag==0:
    print("No")
else:
    print("Yes")
