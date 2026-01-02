from itertools import accumulate,chain



def max_merit(b,l,u):
    return u*(X-b) + l*b

def merit(a,b,l,u):
    return (u if a > b else l)*(a-b) + l*b

N,X = map(int,input().split())

blu = list(tuple(map(int,input().split())) for _ in range(N))
required = sum(l*b for b,l,u in blu)
blu = sorted(((max_merit(*x), x) for x in blu), reverse=True)


for mi,x in enumerate(accumulate(m for m,_ in blu)):
    if x >= required:
        msum2 = x
        msum1 = x - blu[mi][0]
        break

def helper():
    for i,(m,x) in enumerate(blu):
        if i >= mi:
            r = required - msum1
        else:
            r = required + m - msum2

        b,l,u = x
        if r <= l*b:
            yield mi*X + (r-1)//l + 1
        else:
            r -= l*b
            yield mi*X + b + (r-1)//u + 1

print(min(helper()))

