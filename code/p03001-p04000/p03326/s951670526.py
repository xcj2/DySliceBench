n,m = map(int,input().split())
x,y,z = [],[],[]
for i in range(n):
    a,b,c = map(int,input().split())
    x.append(a)
    y.append(b)
    z.append(c)
def ans1(x,y,z,m):
    w = []
    for i in range(n):
        w.append(x[i]+y[i]+z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans2(x,y,z,m):
    w = []
    for i in range(n):
        w.append(x[i]+y[i]-z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans3(x,y,z,m):
    w = []
    for i in range(n):
        w.append(x[i]-y[i]+z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans4(x,y,z,m):
    w = []
    for i in range(n):
        w.append(x[i]-y[i]-z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans5(x,y,z,m):
    w = []
    for i in range(n):
        w.append(-x[i]+y[i]+z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans6(x,y,z,m):
    w = []
    for i in range(n):
        w.append(-x[i]+y[i]-z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans7(x,y,z,m):
    w = []
    for i in range(n):
        w.append(-x[i]-y[i]+z[i])
    w.sort(reverse=True)
    return sum(w[:m])
def ans8(x,y,z,m):
    w = []
    for i in range(n):
        w.append(-x[i]-y[i]-z[i])
    w.sort(reverse=True)
    return sum(w[:m])
ans = max(ans1(x,y,z,m),ans2(x,y,z,m),ans3(x,y,z,m),ans4(x,y,z,m),ans5(x,y,z,m),ans6(x,y,z,m),ans7(x,y,z,m),ans8(x,y,z,m))
print(ans)