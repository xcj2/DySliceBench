n,q=map(int,input().split())
c=input()
s=[input().split() for _ in [0]*q]
def judge(x,opt):
    for y in s:
        if y[0]==c[x]:
            if y[1]=='L':
                x-=1
            else:
                x+=1
            if not opt:
                if x>=n:
                    return False
                elif x<0:
                    return True
            else:
                if x<0:
                    return False
                elif x>=n:
                    return True
    return False
def bisect(l,r,opt):
    center=(r+l)//2
    if judge(center,opt):
        if r-l<=1:
            if not opt:
                return l+1
            else:
                return  n-l
        if not opt:
            return bisect(center+1,r,opt)
        else:
            return bisect(l,center,opt)
    else:
        if r-l<=1:
            if not opt:
                return l
            else:
                return n-r
        if not opt:
            return bisect(l,center,opt)
        else:
            return bisect(center+1,r,opt)
def func():
    l=bisect(0,n,0)
    r=bisect(0,n,1)
    print(n-l-r)
func()