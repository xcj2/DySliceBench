
# # # # class Segtree # # # #

#      0
#   1     2
# 3   4  5  6
#       :
# leaf i - n-1+i
# parent   - (i-1)//2
# children - 2*i+1, 2*i+2

class Segtree:
    # modify UNIT and oper depending on the reduce operation

    UNIT = 0  # sum:0 min:BIG max:-BIG gcd:1 lcm:0 ..

    @classmethod
    def oper(c,x,y):
        return x|y  # sum:+ min/max/gcd/lcm:(same)

    def __init__(s,l):
        s.n = 1
        while s.n<l:
            s.n *= 2
        s.ary = [Segtree.UNIT for i in range(2*s.n-1)]

    def get(s,i):
        return s.ary[i+s.n-1]

    def set(s,i,v):
        k = i+s.n-1
        s.ary[k] = v
        while k>0:
            k = (k-1)//2
            s.ary[k] = Segtree.oper( \
                        s.ary[2*k+1], s.ary[2*k+2])

    def setary(s,a):
        for i,v in enumerate(a):
            s.ary[i+s.n-1] = v
        for k in range(s.n-2,-1,-1):
            s.ary[k] = Segtree.oper( \
                        s.ary[2*k+1], s.ary[2*k+2])

    def query(s,x,y):
        return s.querycore(x,y,0,0,s.n)

    # x,y: from query  k: suffix at focus l,r: range for k
    # right ends (y,r) not included

    def querycore(s,x,y,k,l,r):
        if r<=x or y<=l:
            return Segtree.UNIT
        if x<=l and r<=y:
            return s.ary[k]
        vl = s.querycore(x,y,2*k+1,l,(l+r)//2)
        vr = s.querycore(x,y,2*k+2,(l+r)//2,r)
        return Segtree.oper(vl, vr)

# # # # class Segtree end # # # #

inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()

n = inn()
sgt = Segtree(n)
ss = ins()
s = []
for i in range(n):
    sgt.set(i, 1<<(ord(ss[i])-ord('a')))

#ddprint("tree")
#for c in alpha:
#    ddprint(c)
#    ddprint(tr[c])

q = inn()
for qq in range(q):
    x,y,z = input().split()
    #ddprint(f"x {x} y {y} z {z}")
    if x == '1':
        i = int(y)-1
        c = z
        sgt.set(i, 1<<(ord(c)-ord('a')))
    else:
        l = int(y)
        r = int(z)
        sm = 0
        v = sgt.query(l-1,r)
        for i in range(26):
            if (v>>i)%2==1:
                sm += 1
        print(sm)
