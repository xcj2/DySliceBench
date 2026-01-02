def GCD(a,b):
    if min(a,b)==0:
        return max(a,b)
    else:
        return GCD(min(a,b),max(a,b)%min(a,b))

def _LCM(a,b):
    return a*b//GCD(a,b)

def LCM(array):
    lcm=1
    for i in array:
        lcm=_LCM(lcm,i)
    return lcm

while True:
    n=int(input())
    if n==0:
        break

    d=[]
    v=[]
    for i in range(n):
        _d,_v=[int(j) for j in input().split(" ")]
        d.append(_d)
        v.append(_v)

    V=1
    for i in range(n):
        V=V*v[i]
    array=[d[i]*V//v[i] for i in range(n)]
    lcm=LCM(array)
    for i in range(n):
        print(lcm*v[i]//(V*d[i]))

