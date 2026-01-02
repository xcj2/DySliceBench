x,y,a,b,c=map(int,input().split())
p=[int(i) for i in input().split()]
q=[int(i) for i in input().split()]
r=[int(i) for i in input().split()]
p.append(-1)
q.append(-1)
r.append(-1)
ps=sorted(p)
qs=sorted(q)
rs=sorted(r)
d=0
e=0
f=0
ans=0
def me1():
    global ans
    
    if max(ps[-1],qs[-1],rs[-1])==ps[-1]:
        ans+=ps[-1]
        ps.pop(-1)
        global d
        d+=1
    elif max(ps[-1],qs[-1],rs[-1])==qs[-1]:
        ans+=qs[-1]
        qs.pop(-1)
        global e
        e+=1
    else:
        ans+=rs[-1]
        rs.pop(-1)
        global f
        f+=1
def me2():
    global ans
    if max(ps[-1],rs[-1])==ps[-1]:
        ans+=ps[-1]
        ps.pop(-1)
        global d
        d+=1
    else:
        ans+=rs[-1]
        rs.pop(-1)
        global f
        f+=1
def me3():
    global ans
    if max(qs[-1],rs[-1])==qs[-1]:
        ans+=qs[-1]
        qs.pop(-1)
        global e
        e+=1
    else:
        ans+=rs[-1]
        rs.pop(-1)
        global f
        f+=1
for i in range(x+y):
    #print(ans)
    #print(i)
    
    if d>=x:
        #print('x')
        me3()
    elif e>=y:
        #print('y')
        me2()
    else:
        #print('z')
        me1()
print(ans)
    