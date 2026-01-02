def readinput():
    n = int(input())
    txy = []
    for i in range(n):
        t,x,y = list(map(int,input().split()))
        txy.append((t,x,y))
    return n, txy

def canmove(current, next):
    (t0,x0,y0) = current
    (t1,x1,y1) = next
    dist = abs(x1-x0) + abs(y1-y0)
    tdiff = t1-t0
    if(dist > tdiff):
        return False
    if( tdiff%2 != dist%2 ):
        return False
    return True

def main(n,txy):
    current = (0,0,0)
    for i in range(n):
        next = txy[i]
        ans = canmove(current, next )
        if (ans == False):
            return False
        current = next
    return True

if __name__=='__main__':
    n,txy = readinput()
    ans = main(n,txy)
    if (ans == True):
        print('Yes')
    else:
        print('No')