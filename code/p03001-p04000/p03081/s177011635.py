import sys

N,Q=map(int,input().split())
s=[-1]
s+=list(map(lambda e:ord(e)-65,list(input())))
s+=[-1]
t=[]
d=[]
for i in range(Q):
    ti,di=sys.stdin.readline().rstrip().split()
    ti=ord(ti)-65
    di = -1 if di=='L' else +1
    t.append(ti)
    d.append(di)

def solve(n):
    for i in range(Q):
        if s[n]==t[i]:
            n+=d[i]
    return n

def find_match(x):
    f1 = 1
    f2 = N + 1
    while f1 != f2:
        f3 = (f1 + f2) // 2
        if solve(f3) == x:
            f1 = f3 + 1
        else:
            f2 = f3
    return f1

def find_notmatch(x):
    f1 = 1
    f2 = N + 1
    while f1 != f2:
        f3 = (f1 + f2) // 2
        #print(f1,f2,f3,solve(f3),x)
        if solve(f3) != x:
            f1 = f3 + 1
        else:
            f2 = f3
    return f1

#for i in range(1,N+1):
#    print(solve(i))

print(find_notmatch(N+1)-find_match(0))
