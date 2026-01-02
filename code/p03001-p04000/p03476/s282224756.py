def prime(n):
    a = [1]*(n+1)
    a[0],a[1] = 0,0
    for i in range(2,int(n**(0.5))+1):
        j = 2
        while i*j <= 10**5:
            a[i*j] = 0
            j += 1
    return a

def like2017(a):
    c = [0]*(10**5+1)
    for i in range(3,10**5+1):
        if a[i]*a[(i+1)//2]:
            c[i] = 1
    return c

def ssum(c):
    s = [0]*(10**5+1)
    for i in range(2,10**5+1):
        s[i] = s[i-1]+c[i]
    return s

def s(lst,l,r):
    return lst[r]-lst[l-1]


q = int(input())
a = prime(10**5)
c = like2017(a)

ss = ssum(c)
for i in range(q):
    l,r = map(int,input().split())
    print(s(ss,l,r))