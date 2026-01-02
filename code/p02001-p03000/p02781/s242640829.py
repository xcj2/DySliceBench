import math
n=int(input())
k=int(input())
strn=str(n)

ans1=9*(len(strn)-1)+int(strn[0])
#print(ans1)

def fuc1(x):
    strn=str(x)
    return 9*(len(strn)-1)+int(strn[0])

def fuc2(x):
    if x<10:
        return 0
    strn=str(x)
    ans2=fuc1(int(strn[1:]))
    ans2+=(int(strn[0])-1)*(9*(len(strn)-1))
    #print(ans2,"q")
    for i in range(1,len(strn)-1):
        ans2+=9*(9*(len(strn)-i-1))
    return ans2

def fuc3(x):
    if x<100:
        return 0
    ans3=fuc2(int(strn[1:]))
    ans3+=(int(strn[0])-1)*(81*(len(strn)-1)*(len(strn)-2)//2)
    #print(ans3,"z")
    for i in range(1,len(strn)-2):
        ans3+=9*(81*(len(strn)-i-1)*(len(strn)-i-2)//2)
    #print(ans3)
    return ans3

if k==1:
    print(fuc1(n))
if k==2:
    print(fuc2(n))
if k==3:
    print(fuc3(n))