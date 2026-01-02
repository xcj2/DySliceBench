def s(n):
    return[m(t)for t in d(f(n))]
def f(n):
    l=[]
    b,e=2,0
    while b*b<=n:
        while not n%b:
            n//=b
            e+=1
        if e:
            l.append((b,e))
        b,e=b+1,0
    if n>1:
        l.append((n,1))
    return l
def d(l):
    b,e=l.pop()
    p=d(l)if l else[[]]
    v=[[(b,k)]for k in range(e+1)]
    return[s+t for s in p for t in v]
def m(l):
    a=1
    for b,e in l:
        a*=b**e
    return a
N,M=map(int,input().split())
if M<2:print(1);exit()
a=0
for i in sorted(s(M))[::-1]:
    if M//i>=N:
        a=i
        break
print(a)