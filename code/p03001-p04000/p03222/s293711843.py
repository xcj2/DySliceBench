def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper

@memoize
def line_num(n):
    if n<=0:
        return 1
    elif n==1:
        return 2
    elif n==2:
        return 3
    else:
        return line_num(n-1) + line_num(n-2)

@memoize
def ans(h,w,k):
    if w==1:
        return 1
    elif h==1: # w>=2
        if k == 1:
            return line_num(w-2)
        elif k == 2:
            return line_num(w-3)
        else:
            return 0
    else:
        if k==1:
            return ans(h-1,w,k)*line_num(w-2) + ans(h-1,w,k+1)*line_num(w-3)
        elif k==w:
            return ans(h-1,w,k)*line_num(w-2) + ans(h-1,w,k-1)*line_num(w-3)
        else:
            a = ans(h-1,w,k)*(line_num(k-2)*line_num(w-k-1))
            b = ans(h-1,w,k-1)*(line_num(k-3)*line_num(w-k-1))
            c = ans(h-1,w,k+1)*(line_num(k-2)*line_num(w-k-2))
            return a+b+c

M = 1000000007

h,w,k = map(int,input().split())

print(ans(h,w,k) % M)