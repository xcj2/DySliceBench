import sys

def solve():
    for line in sys.stdin:
        xa,ya,xb,yb,xc,yc,xd,yd = map(float, line.split(','))
        
        def fac(x, y):
            if xa == xc:
                return x - xa
            else:
                return ((ya-yc)/(xa-xc))*(x-xa) - y + ya
        
        def fbd(x, y):
            if xb == xd:
                return x - xb
            else:
                return ((yb-yd)/(xb-xd))*(x-xb) - y + yb
        
        if fac(xb, yb) * fac(xd, yd) > 0:
            print('NO')
        elif fbd(xa, ya) * fbd(xc, yc) > 0:
            print('NO')
        else:
            print('YES')

if __name__ == "__main__":
    solve()

