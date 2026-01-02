def ctoi(x):
    return ord(x)-ord("a")
n = int(input())
s = list(input())
q = int(input())
bit = [[0]*(n+1) for _ in range(26)]

def update(pos,a,x):
    while pos<=n:
        bit[a][pos] += x
        pos += pos&(-pos)

def query(pos):
    ret=[0]*26
    for i in range(26):
        tmp=0
        p=pos
        while p>0:
            tmp+=bit[i][p]
            p-=p&(-p)
        ret[i]=tmp
    return ret

for i in range(n):
    update(i+1,ctoi(s[i]),1)

for _ in range(q):
    flag,a,b = input().split()
    flag=int(flag)
    a=int(a)
    if flag==1:
        if s[a-1]==b:
            continue
        else:
            update(a,ctoi(s[a-1]),-1)
            update(a,ctoi(b),1)
            s[a-1]=b
    else:
        b=int(b)
        c1 = query(b)
        c2 = query(a-1)
        ans = 0
        for i in range(26):
            if c1[i]-c2[i]>0:
                ans += 1
        print(ans)