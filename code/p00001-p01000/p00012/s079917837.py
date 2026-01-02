def point(a,b):
    return a[0]*b[0]+a[1]*b[1]
def euclid(a):
    return (a[0]**2+a[1]**2)**(1/2)
def cos(a,b):
    return point(a,b)/(euclid(a)*euclid(b))
while 1:
    try:
        ax,ay,bx,by,cx,cy,px,py = map(float, input().split(" "))
        ab = [bx-ax, by-ay]
        ac = [cx-ax, cy-ay]
        ba = [ax-bx, ay-by]
        bc = [cx-bx, cy-by]
        ap = [px-ax, py-ay]
        bp = [px-bx, py-by]
        if min(cos(ab,ap),cos(ac,ap)) > cos(ab,ac) and min(cos(ba,bp),cos(bc,bp)) > cos(ba,bc):
            print("YES")
        else:
            print("NO")
    except:
        break
