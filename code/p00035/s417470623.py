#凸包を求める

def quickhull(l,r,s,k):
    if not s:
        return
    su = []
    sd = []
    a = (r[0]-l[0],r[1]-l[1])
    for x,y in s:
        b = (x-l[0],y-l[1])
        cro = cross(a,b)
        if cro > 0:
            su.append((x,y)) #上半分
        elif cro < 0:
            sd.append((x,y)) #下半分

    if su:
        c,d = direction(l,r,su[0])
        p = su[0]
        for i in range(1,len(su)):
            c_,d_ = direction(l,r,su[i])
            if c*d_ < c_*d:
                c,d = c_,d_
                p = su[i]
        k.append(tuple(p)) #もっとも離れた点を凸包の頂点に追加
        b = (l[0]-p[0],l[1]-p[1])
        c = (p[0]-r[0],p[1]-r[1])
        s1 = []
        s2 = []
        for x,y in su:
            b_ = (x-p[0],y-p[1])
            c_ = (x-r[0],y-r[1])
            cro_b,cro_c = cross(b,b_),cross(c,c_)
            if cro_b >= 0 and cro_c >= 0: #三角形内部判定
                continue
            else:
                if cro_b < 0:
                    s1.append((x,y))
                elif cro_c < 0:
                    s2.append((x,y))
        quickhull(l,p,s1,k) #再帰
        quickhull(p,r,s2,k)

    if sd:
        c,d = direction(l,r,sd[0])
        p = sd[0]
        for i in range(1,len(sd)):
            c_,d_ = direction(l,r,sd[i])
            if c*d_ < c_*d:
                c,d = c_,d_
                p = sd[i]
        k.append(tuple(p)) #もっとも離れた点を凸包の頂点に追加
        b = (l[0]-p[0],l[1]-p[1])
        c = (p[0]-r[0],p[1]-r[1])
        s1 = []
        s2 = []
        for x,y in sd:
            b_ = (x-p[0],y-p[1])
            c_ = (x-r[0],y-r[1])
            cro_b,cro_c = cross(b,b_),cross(c,c_)
            if cro_b <= 0 and cro_c <= 0: #三角形内部判定(ベクトルの向きにより上下で判定が異なることに注意)
                continue
            else:
                if cro_b > 0:
                    s1.append((x,y))
                elif cro_c > 0:
                    s2.append((x,y))
        quickhull(l,p,s1,k) #再帰
        quickhull(p,r,s2,k)
    return k

def cross(a,b): #外積
    return a[0]*b[1]-a[1]*b[0]

def direction(l,r,p): #点と直線の距離
    a = r[1]-l[1]
    b = l[0]-r[0]
    return (a*(p[0]-l[0])+b*(p[1]-l[1]))**2, a**2+b**2 #分子の2乗,分母の2乗
while 1:
    try:
        t = [float(x) for x in input().split(",")]
        s = []
        for i in range(len(t)//2):
            s.append((t[2*i],t[2*i+1]))
        s.sort()
        l = tuple(s.pop(0))
        r = tuple(s.pop(-1))
        k = quickhull(l,r,s,[l,r])
        if len(k) < 4:
            print("NO")
        else:
            print("YES")
    except:
        quit()

