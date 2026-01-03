# Treap
#平衡二分木　乱数を用いてできるだけ平衡を保つらしい　
#priorityには乱数を入れること
# d = 0: right rotation
# d = 1: left rotation
def rotate(nd, d):
    c = nd[d]
    if d:
        e = c[1]
        nd[1] = c[0]
        c[0] = nd
    else:
        e = c[0]
        nd[0] = c[1]
        c[1] = nd

    r = c[4] = nd[4]
    nd[4] = r - (e[4] if e else 0) - 1
    return c

# insert a node with key = val and priority = pri
root = None
def insert(val, pri):
    global root
    st = []
    dr = []
    x = root
    while x:
        st.append(x)
        if x[2] == val:
            return
        d = (x[2] < val)
        dr.append(d)
        x = x[d]

    # [<left>, <right>, <key>, <priority>, <count>]
    nd = [None, None, val, pri, 1]
    while st:
        x = st.pop(); d = dr.pop()
        x[d] = nd
        x[4] += 1
        if x[3] >= nd[3]:
            break
        rotate(x, d)
    else:
        root = nd

    for x in st:
        x[4] += 1

def __delete(nd):
    st = []; dr = []
    while nd[0] or nd[1]:
        l = nd[0]; r = nd[1]
        d = (l[3] <= r[3]) if l and r else (l is None)
        st.append(rotate(nd, d))
        dr.append(d ^ 1)
    nd = x = None
    while st:
        nd = x; x = st.pop(); d = dr.pop()
        x[d] = nd
        x[4] -= 1
    return x

def delete(val):
    global root
    x = root

    st = []
    y = None
    while x:
        if val == x[2]:
            break
        y = x; d = (x[2] < val)
        st.append(y)
        x = x[d]
    else:
        return

    if y:
        y[d] = __delete(x)
        for x in st:
            x[4] -= 1
    else:
        root = __delete(x)

def find(val):
    global root
    x = root
    while x:
        if val == x[2]:
            return 1
        x = x[x[2] < val]
    return 0

import random

def small(val):
    global root
    x=root
    ans=0
    while x:
        if x[2]>val:
            x=x[0]
        elif x[2]<val:
            if x[0]:
                ans+=x[0][4]+1
            else:
                ans+=1
            x=x[1]
    return ans

import random,sys

input=sys.stdin.readline

N,K=map(int,input().split())
A=[]
for i in range(0,N):
    a=int(input())-K
    A.append(a)

for i in range(1,N):
    A[i]+=A[i-1]

A=[0]+A
A=[(A[i],i) for i in range(0,N+1)]
A.sort()
A=[A[i][1] for i in range(0,N+1)]
ans=0
for i in range(0,N+1):
    ans+=small(A[i])
    insert(A[i],random.randint(0,100000))

print(ans)