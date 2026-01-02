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

def search1(val):
    global root
    x = root
    ans=-1
    while x:
        if val==x[2]:
            return val
        if val>x[2]:
            ans=max(ans,x[2])
            if x[1]==None:
                return ans
            else:
                x=x[1]
        if val<x[2]:
            if x[0]==None:
                return ans
            else:
                x=x[0]
    return ans

def search2(val):
    global root,N
    x=root
    ans=N
    while x:
        if val==x[2]:
            return val
        if val>x[2]:
            if x[1]==None:
                return ans
            else:
                x=x[1]
        if val<x[2]:
            ans=min(ans,x[2])
            if x[0]==None:
                return ans
            else:
                x=x[0]
    return ans

import random

N=int(input())
P=list(map(int,input().split()))
dic={key:-1 for key in range(1,N+1)}
for i in range(0,N):
    dic[P[i]]=i

answer=0
for i in range(0,N):
    k=N-i
    l1=search1(dic[k])
    l2=search1(l1-1)
    r1=search2(dic[k])
    r2=search2(r1+1)
    answer+=k*(dic[k]-l1)*(r2-r1)+k*(l1-l2)*(r1-dic[k])
    insert(dic[k],random.randint(1,100000))

print(answer)