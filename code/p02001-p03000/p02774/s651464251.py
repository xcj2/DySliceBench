from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def dominus(t):
    r = len(plus)-1
    ans = 0
    for m in minus:
        while r>=0 and m*plus[r] >= -t:
            r -= 1
            if r<0:
                break
        ans += len(plus)-r-1
        #ddprint("m {} r {} pr {}".format(m,r,plus[r]))
    #ddprint("domin t {} ans {}".format(t,ans))
    return ans

def doplus(t):
    return doplus1(t,plus)+doplus1(t,minus)

def doplus1(t,b):
    ans = 0
    r = 0
    for i in range(len(b)-1,0,-1):
        p = b[i]
        r = min(r,i-1)
        while p*b[r] <= t:
            r += 1
            if r>=i:
                break
        ans += r
    #ddprint("p1 t {} b {} ans {}".format(t,b,ans))
    return ans

n,k = inm()
a = inl()
plus = []
minus = []
nzero = 0
for x in a:
    if x<0:
        minus.append(-x)
    elif x>0:
        plus.append(x)
    else:
        nzero += 1
minus.sort()
plus.sort()
kminus = len(plus)*len(minus)
kzero = (2*n-1-nzero)*nzero//2
kmz = kminus+kzero
ddprint("n {} k {}".format(n,k))
ddprint("minus")
ddprint(minus)
ddprint(plus)
if kminus<k<=kminus+kzero:
    print(0)
else:
    dom = (kminus>=k)
    if not dom:
        mn = 0
        mx = 10**19
        while mx>mn+1:
            mid = (mx+mn)//2
            v = doplus(mid)
            if v>=k-kmz:
                mx = mid
            else:
                mn = mid
            #ddprint("ploop mn {} mx {} mid {} v {} k {} kmz {}".format(mn,mx,mid,v,k,kmz))
    else:
        mx = 0
        mn = -10**19
        while mx>mn+1:
            mid = (mx+mn)//2
            v = dominus(mid)
            if v>=k:
                mx = mid
            else:
                mn = mid
            #ddprint("mn {} mx {} mid {} v {} k {}".format(mn,mx,mid,v,k))
    print(mx)
