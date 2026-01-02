from copy import copy
S=input()
S+="A"
lst1=[]
lst2=[]
lst3=[]
lst1.append(int(S[0]))
lst2.append(0)
def confirm(l1,l2):
    s=0
    for i in range(len(l1)):
        if l2[i]==0:
            s+=l1[i]
        else:
            s-=l1[i]
    return s
def draw(l1,l2,l3):
    s=""
    for i in range(len(l1)):
        if l2[i]==0:
            s=s+"+"+str(l1[i])
        else:
            s=s+"-"+str(l1[i])
    s=s+"=7"
    l3.append(s[1:])
    return 0
def func(S,l1,l2,l3):
    if S=="A":
        if confirm(l1,l2)==7:
            draw(l1,l2,l3)
            return 0
        return 0
    x=copy(l1)
    x.append(int(S[0]))
    y1=copy(l2)
    y1.append(0)
    y2=copy(l2)
    y2.append(1)
    return func(S[1:],x,y1,l3),func(S[1:],x,y2,l3)
func(S[1:],lst1,lst2,lst3)
print(lst3[0])