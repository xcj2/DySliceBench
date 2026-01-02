def ii2ss(n):
    ss = []
    for i in range(n):
        ss.append(input())
    return ss

def sp2nn(sp, sep=' '):
    return [int(s) for s in sp.split(sep)]

def ss2nn(ss):
    return [int(s) for s in list(ss)]

def tk(i, j, k):
    return '%d %d %d' % (i, j, k)

def tkr(key):
    return sp2nn(key)

def main(ss):
    X, Y, Z, K = sp2nn(ss[0])
    aa = sp2nn(ss[1])
    bb = sp2nn(ss[2])
    cc = sp2nn(ss[3])
    aa.sort()
    aa.reverse()
    bb.sort()
    bb.reverse()
    cc.sort()
    cc.reverse()
    
    d = {}
    st = set()
    key = tk(0, 0, 0)
    st.add(key)
    d[key] = aa[0] + bb[0] + cc[0]
    for _ in range(K):
        vmax = -1
        vk = ''
        for k, v in d.items():
            if vmax < v:
                vmax = v
                vk = k
        print(vmax)
        d.pop(vk)
        st.add(vk)
        i, j, k = tkr(vk)
        if i + 1 < len(aa):
            key = tk(i+1, j, k)
            if key not in st:
                d[key] = aa[i+1] + bb[j] + cc[k]
        if j + 1 < len(bb):
            key = tk(i, j+1, k)
            if key not in st:
                d[key] = aa[i] + bb[j+1] + cc[k]
        if k + 1 < len(cc):
            key = tk(i, j, k+1)
            if key not in st:
                d[key] = aa[i] + bb[j] + cc[k+1]
        
main(ii2ss(4))