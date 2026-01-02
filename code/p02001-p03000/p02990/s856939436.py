def extEuclid(x, y, debug=False):
    """
    Param:
        x, y - coeffcients
        debug - print an equation
    Return:
        a tuple of integer (a, b) satisfying xa + yb = 1
    """
    changed = False
    if x < y:
        tmp = x
        x = y
        y = tmp
        changed = True
    if x % y == 0:
        raise ValueError("extEuclid: x, y not coprime or x = 1 or y = 1")
    
    alist = [x]
    blist = [y]
    a,b = x,y
    q = a // b
    r = a % b
    qlist = [q]
    rlist = [r]
    while r != 0:
        a = b
        b = r
        q = a//b
        r = a%b
        alist.append(a)
        blist.append(b)
        qlist.append(q)
        rlist.append(r)
    N = len(qlist)

    if rlist[N-2] != 1:
        raise ValueError("extEuclid: x, y not coprime")
    
    s = [1]
    t = [-qlist[N-2]]
    for i in range(N-2):
        s.append(t[i])
        t.append(s[i]+t[i]*(-qlist[N-3-i]))
    
    if(debug):
        print("("+str(x)+")*("+str(s[len(s)-1])+")+("+str(y)+")*("+str(t[len(t)-1])+") = 1")
    
    if not changed:
        return (s[len(s)-1], t[len(t)-1])
    else:
        return (t[len(t)-1], s[len(s)-1])

N, K = map(int,input().split())
mod = 10**9+7
f = [None for i in range(N+1)] # fs[i] = i!
for i in range(N+1):
    if i == 0:
        f[i] = 1
    else:
        f[i] = (f[i-1] * i) % mod

def inv(x):
    res = 1
    k = mod - 2
    y = x
    while k:
        if (k & 1):
            res = (res * y) % mod
        y = (y * y) % mod
        k //= 2
    
    return res

def conb(n, k):
    fn = f[n]
    fm = f[n-k]
    fk = f[k]

    fmk = (fm * fk) % mod

    return (fn * inv(fmk)) % mod
for i in range(1, K+1):
    if N - K + 1 < i:
        print(0)
    else:
        print(conb(N-K+1, i)*conb(K-1, i-1) % mod)
