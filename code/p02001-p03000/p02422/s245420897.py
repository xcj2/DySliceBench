def hyouji(moji,a,b):
    for j in range(a,b):
        print(moji[j],end="")
    print()

def gyakujun(moji,a,b):
    moji1=[moji[i] for i in range(a,b)]
    moji1.reverse()
    for i in range(a,b):
        moji[i]=moji1[i-a]
    return moji
    
def replace(moji,a,b,p):
    for i in range(a,b):
        moji[i]=p[i-a]
    return moji

nyuryoku=input()
moji=[]

for i in nyuryoku:
    moji.append(i)

kaisu=int(input())

for j in range(kaisu):
    command=list(map(str,input().split()))
    p=[]
    meirei=command[0]
    a=int(command[1])
    b=int(command[2])+1
    if len(command)==4:
        for i in command[3]:
            p.append(i)
    if meirei=="print":
        hyouji(moji,a,b)
    elif meirei=="reverse":
        gyakujun(moji,a,b)
    elif meirei=="replace":
        replace(moji,a,b,p)

