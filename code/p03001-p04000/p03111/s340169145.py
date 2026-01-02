def solve(n, a, b, c, l):
    v = gen(a,b,c,l,n,0,[],[],[])
    print(v)

    
def gen(a,b,c,l,n,idx,al,bl,cl):
    if idx == n:
        if (len(al) > 0) and (len(bl) > 0) and (len(cl) > 0):
            v = calc(a,b,c,al,bl,cl)
            # print(f"{a}:{al}, {b}:{bl}, {c}:{cl} => {v}")
            return v
        else:
            return 3000

    l1 = l[idx]
    nal = al.copy()
    nbl = bl.copy()
    ncl = cl.copy()

    nal.append(l1)
    nbl.append(l1)
    ncl.append(l1)

    va = gen(a, b, c, l, n, (idx+1), nal,bl,cl)
    vb = gen(a, b, c, l, n, (idx+1), al,nbl,cl)
    vc = gen(a, b, c, l, n, (idx+1), al,bl,ncl)
    vn = gen(a, b, c, l, n, (idx+1), al,bl,cl)
    return min(va, vb, vc, vn)

def calc(a,b,c,al,bl,cl):
    mp = 0
    
    t = al
    mp += (len(t) - 1) * 10
    length = sum(t)
    mp += abs(a - length)

    t = bl
    mp += (len(t) - 1) * 10
    length = sum(t)
    mp += abs(b - length)

    t = cl
    mp += (len(t) - 1) * 10
    length = sum(t)
    mp += abs(c - length)

    return mp
    
n, a, b, c = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))

solve(n, a, b, c, sorted(l))
