def op(x,y):
    """
    Outer product
    """
    return(complex.conjugate(x)*y).imag

def isrm(q,i,x):   
    """
    is i right most to q's from view of x?
    """
    for j in q:
        if op(i-x, j-x) < 0:
            return(False)
    return(True)

def rightmost(p,x):
    """
    Find a point in p which is rightmost from x(other than x)
    """
    for i in [i for i in p if i!=x]:
        q = p.copy()
        q.remove(i)
        if isrm(q,i,x):
            return(i)
    raise ValueError('Do not come here')

def solve(p,pf,orig):
    nx = rightmost(p,orig)
    ni = p.index(nx)
    if pf[ni]:   # second visit
        return(pf)
    pf[ni] = True
    return(solve(p,pf,nx))

while True:
    p = []
    n = int(input().strip())
    if n==0:
        break
    for i in range(n):
        x,y = list(map(float, input().strip().split(',')))
        p.append(x+y*1j)
    print(solve(p,[False for _ in range(n)],2000.0 + 0.0*1j).count(False))