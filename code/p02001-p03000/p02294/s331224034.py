def dot(a,b):return a[0]*b[0] + a[1]*b[1]
def cross(a,b):return a[0]*b[1] - a[1]*b[0]
def isOn(a,b):
    if cross(a,b) == 0:
        if dot(a,b) < 0 or dot(a,a) < dot(b,b) : return False
        else : return True
    else : 
        return False

q = int(input())
for i in range(q):
    x0,y0,x1,y1,x2,y2,x3,y3 = [int(i) for i in input().split()]
    a = [x1-x0,y1-y0]
    b = [x2-x0,y2-y0]
    c = [x3-x0,y3-y0]
    d = [x3-x2,y3-y2]
    e = [x0-x2,y0-y2]
    f = [x1-x2,y1-y2]
    if isOn(a,b) or isOn(a,c):
        print(1)
    elif cross(a,b) == 0 and cross(a,c) == 0:
        if ( not isOn(c,a) and isOn(b,a)) or (isOn(c,a) and not isOn(b,a)) :
            print(1)
        else:
            print(0)
    elif cross(a,b) * cross(a,c) > 0 :
        print(0)
    elif cross(d,e) * cross(d,f) > 0 :
        print(0)
    else :
        print(1)