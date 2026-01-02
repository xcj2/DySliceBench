printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def cmp1(a,b):
    l = []
    for i in range(len(a)):
        ok = True
        for j in range(min(len(b),len(a)-i)):
            #ddprint("a {} b {} i {} j {}".format(a,b,i,j))
            #ddprint("aij {} bj {}".format(a[i+j],b[j]))
            if a[i+j]!='?' and b[j]!='?' and a[i+j]!=b[j]:
                ok = False
                break
        if ok:
            l.append(i)
    #ddprint("cmp1 a {} b {} l {}".format(a,b,l))
    return l

def chk3(mn,a,b,c,ab,ac,bc):
    for i in ab:
        v = max(len(a),len(b)+i)+len(c)
        mn = min(mn,v)
        for j in bc:
            if len(a)-i<=j or (j+i) in ac:
                v = max([len(a),len(b)+i,len(c)+i+j])
                mn = min(mn,v)
        for j in ac:
            if len(b)+i<=j:
                v = max(len(a),len(c)+j)
                mn = min(mn,v)

    for i in bc:
        v = max(len(b),len(c)+i)+len(a)
        mn = min(mn,v)
    return mn

def solve(a,b,c):
    ab = cmp1(a,b)
    ac = cmp1(a,c)
    bc = cmp1(b,c)
    ba = cmp1(b,a)
    ca = cmp1(c,a)
    cb = cmp1(c,b)
    mn = len(a)+len(b)+len(c)
    ddprint(mn)
    mn = chk3(mn,a,b,c,ab,ac,bc)
    ddprint(mn)
    mn = chk3(mn,a,c,b,ac,ab,cb)
    ddprint(mn)
    mn = chk3(mn,b,a,c,ba,bc,ac)
    ddprint(mn)
    mn = chk3(mn,b,c,a,bc,ba,ca)
    ddprint(mn)
    mn = chk3(mn,c,a,b,ca,cb,ab)
    ddprint(mn)
    mn = chk3(mn,c,b,a,cb,ca,ba)
    return mn

a = ins()
b = ins()
c = ins()
mn = solve(a,b,c)
print(mn)
