def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def LIR(n): return [LI() for i in range(n)]
def MI(): return map(int, input().split())

#1
#1_A
"""
x,y,s,t = map(float, input().split())
a = int(input())
s-=x
t-=y
while a:
    a -= 1
    p,q = map(float, input().split())
    p-=x
    q-=y
    ans_x = s*(q*t+p*s)/(t*t+s*s)
    ans_y = t*(q*t+p*s)/(t*t+s*s)
    print(x+ans_x, y+ans_y)
"""

#1_B
"""
p1x,p1y,c,d = MI()
q = II()
if p1x == c:
    f = 0
elif p1y == d:
    f = 1
else:
    f = 2
    m = (d-p1y)/(c-p1x)
for _ in range(q):
    px,py = MI()
    if not f:
        a = 2*p1x-px
        b = py
    elif f == 1:
        a = px
        b = 2*p1y-py
    else:
        a = (2*py+(1/m-m)*px+2*m*p1x-2*p1y)/(m+1/m)
        b = -1/m*(a-px)+py
    print(a,b)
"""

#1_C
"""
def inner_product(a,b):
    return a[0]*b[0]+a[1]*b[1]

def cross_product(a,b):
    return a[0]*b[1]-a[1]*b[0]
p,q,c,d = MI()
a = [c-p,d-q]
r = II()
for _ in range(r):
    c,d = MI()
    b = [c-p,d-q]
    co = inner_product(a,b)
    si = cross_product(a,b)
    if si == 0:
        if co >= 0:
            if a[0]**2+a[1]**2 >= b[0]**2+b[1]**2:
                print("ON_SEGMENT")
            else:
                print("ONLINE_FRONT")
        else:
            print("ONLINE_BACK")
    elif si > 0:
        print("COUNTER_CLOCKWISE")
    else:
        print("CLOCKWISE")
"""

#2
#2_A
def inner_product(a,b):
    return a[0]*b[0]+a[1]*b[1]

def cross_product(a,b):
    return a[0]*b[1]-a[1]*b[0]
q = II()
for i in range(q):
    s,t,a,b,x,y,c,d = MI()
    a = [a-s,b-t]
    b = [c-x,d-y]
    co = inner_product(a,b)
    si = cross_product(a,b)
    if not si:
        print(2)
    elif not co:
        print(1)
    else:
        print(0)

