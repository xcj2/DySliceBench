def f(x,y,z):
    if x=="S" and y=="o":
        return z
    if x=="S" and y=="x":
        return g(z)
    if x=="W" and y=="o":
        return g(z)
    if x=="W" and y=="x":
        return z
def g(x):
    if x=="S":
        return "W"
    if x=="W":
        return "S"
def check(x,y):
    t[0]=x
    t[1]=y
    for j in range(1,N-1):
        t[j+1] = f(t[j],s[j],t[j-1])
    x1 = f(t[N-1],s[N-1],t[N-2])
    y1 = f(x1,s[0],t[N-1])
    if x==x1 and y==y1:
        return True
    else:
        return False
N = int(input())
s = input().strip()
t = [0 for _ in range(N)]
if check("S","S"):
    print("".join(t))
elif check("S","W"):
    print("".join(t))
elif check("W","S"):
    print("".join(t))
elif check("W","W"):
    print("".join(t))
else:
    print(-1)