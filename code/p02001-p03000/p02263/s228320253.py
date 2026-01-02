def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/float(y)

a=input().split()
i=0
for j in range(len(a)):
    if a[i]=="+":
        a[i-2]=int(a[i-2])
        a[i-1]=int(a[i-1])
        a[i]=int(add(a[i-2],a[i-1]))
        del a[i-2]
        del a[i-2]
        i=i-2
    elif a[i]=="-":
        a[i-2]=int(a[i-2])
        a[i-1]=int(a[i-1])
        a[i]=int(sub(a[i-2],a[i-1]))
        del a[i-2]
        del a[i-2]
        i=i-2
    elif a[i]=="*":
        a[i-2]=int(a[i-2])
        a[i-1]=int(a[i-1])
        a[i]=int(mul(a[i-2],a[i-1]))
        del a[i-2]
        del a[i-2]
        i=i-2
    elif a[i]=="/":
        a[i-2]=int(a[i-2])
        a[i-1]=int(a[i-1])
        a[i]=int(div(a[i-2],a[i-1]))
        del a[i-2]
        del a[i-2]
        i=i-2
    i=i+1
print(a[0])

