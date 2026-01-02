#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def dfs(n):
    global h
    if n in h:
        return h[n]
    #ddprint(f"dfs {n}")
    if n==1:
        return d
    v1 = n*d
    v3 = v5 = BIG
    if n%2==1:
        v2a = dfs((n-1)//2)+a+d
        v2b = dfs((n+1)//2)+a+d
        v2 = min(v2a,v2b)
    else:
        v2 = dfs(n//2)+a

    if n>=3:
        r = n%3
        if r<=1:
            v3 = dfs((n-r)//3)+b+r*d
        else:
            v3 = dfs((n+1)//3)+b+d

    if n>=5:
        r = n%5
        if r<=2:
            #ddprint(f"dfs {n} v5 b {b} r {r} d {d}")
            v5 = dfs((n-r)//5)+c+r*d
        else:
            v5 = dfs((n+5-r)//5)+c+(5-r)*d

    ret = min([v1,v2,v3,v5])
    h[n] = ret
    #ddprint(f"dfs {n} v1235 {v1} {v2} {v3} {v5} rtn {ret}")
    return ret

k = 400
def foo(n):
    if n<=k:
        return dfs(n)
    v1 = n*d
    m = n
    sm = 0
    while m>k:
        if m%2==1:
            if m%4==1:
                m -= 1
            else:
                m += 1
            sm += d
        m //= 2
        sm += a
    v2 = dfs(m)+sm

    m = n
    sm = 0
    while m>k:
        r = m%3
        if r==1:
            m -= 1
            sm += d
        elif r==2:
            m += 1
            sm += d
        m //= 3
        sm += b
    v3 = dfs(m)+sm

    m = n
    sm = 0
    while m>k:
        r = m%5
        if r<=2:
            m -= r
            sm += r*d
        else:
            m += 5-r
            sm += (5-r)*d
        m //= 5
        sm += c
    v5 = dfs(m)+sm

    #ddprint(f"foo v1235 {v1} {v2} {v3} {v5}")
    return min([v1,v2,v3,v5])

t = inn()
for tt in range(t):
    n,a,b,c,d = inm()
    h = {}
    print(dfs(n))
