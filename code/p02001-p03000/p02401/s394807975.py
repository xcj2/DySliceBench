def wa(a,b,output):
    output=a+b
    return output

def sa(a,b,output):
    output=a-b
    return output

def seki(a,b,output):
    output=a*b
    return output

def syou(a,b,output):
    output=a//b
    return output

num=list(map(str,input().split()))
out=[]
while num[1]!="?":
    output=0
    a=int(num[0])
    b=int(num[2])

    if num[1]=="+":
        output=wa(a,b,output)
    elif num[1]=="-":
        output=sa(a,b,output)
    elif num[1]=="*":
        output=seki(a,b,output)
    elif num[1]=="/":
        output=syou(a,b,output)
    out.append(output)
    num=list(map(str,input().split()))

for i in range(len(out)):
    print(out[i])

