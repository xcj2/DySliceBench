N = int(input())
A = list(map(int,input().split()))

def last_value(x):
    tmp2 = x
    for a in A:
        tmp = x
        x = a - tmp
    return x-tmp2

def bsearch(l,r):
    if l > r:
        return -1
    else:
        c = (l+r)//2
        last = last_value(c)
        if last < 0:
            return bsearch(l,c-1)
        elif last> 0:
            return bsearch(c+1,r)
        elif last == 0:
            return c
    
    
        
def solver(x):
    ans = [0] * N
    ans[0] = x*2
    for i,a in enumerate(A[:-1]):
        tmp = x
        x = a - tmp
        ans[i+1] = x * 2
    return ans


Left = 0
Right = min(A[0],A[N-1])

ans = solver(bsearch(Left,Right))

print(' '.join(map(str,ans)))