import math

def sub(a, b):
    return [x-y for x,y in zip(a,b)]

def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def abs2(a):
    return sum([x*x for x in a])

def deg(a, b):
    return (math.acos(dot(a,b)/math.sqrt(abs2(a)*abs2(b))))

N,Q = map(int,input().split())
ls = [list(map(int,input().split())) for i in range(N)]

for i in range(Q):
    sx,sy,sz,dx,dy,dz = map(int,input().split())
    cost = 0
    s = [sx,sy,sz]
    d = [dx,dy,dz]
    sd = sub(d,s)
    ds = sub(s,d)
    for v in ls:
        if abs(deg(sub(v[:3],s),sd)) < math.pi/2 and abs(deg(sub(v[:3],d), ds)) < math.pi/2:
            if abs2(cross(sub(v[:3],s),sd)) <= abs2(sd)*v[3]**2:
                cost += v[4]
        else:
            if min(abs2(sub(v[:3],s)), abs2(sub(v[:3],d))) <= v[3]**2:
                cost += v[4]
    print(cost)
