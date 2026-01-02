from collections import defaultdict

def parse_expr(s,i,num):
    if i < len(s) and f_num[s[i]]:
        n,i = parse_num(s,i,num)
        if s[i] == "(":
            i += 1
            su = 0
            while i < len(s) and s[i] != ")":
                e,i = parse_expr(s,i,num)
                su += e
            return su*n,i+1
        else:
            k,i = parse_alp(s,i,n)
            return k+n-1,i
    else:
        k,i = parse_alp(s,i,num)
        return k,i

def parse_num(s,i,num):
    m = int(s[i])
    i += 1
    while i < len(s) and f_num[s[i]]:
        m *= 10
        m += int(s[i])
        i += 1
    return num*m,i

def parse_alp(s,i,num):
    k = 1
    i += 1
    while i < len(s) and f_alp[s[i]]:
        k += 1
        i += 1
    return k,i

def find(s,l,r,i):
    if l == r:
        return 0
    su,k = parse_expr(s,l,1)
    if i < su:
        if l < r and f_alp[s[l]]:
            return s[l+i]
        else:
            n,l = parse_num(s,l,1)
            if l < r and s[l] == "(":
                return find(s,l+1,k-1,i%(su//n))
            else:
                return find(s,l,k,i%(su//n))
    else:
        return find(s,k,r,i-su)
while 1:
    s,i = input().split()
    if s == i == "0":break
    i = int(i)
    f_alp = defaultdict(lambda : 0)
    f_num = defaultdict(lambda : 0)
    for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        f_alp[a] = 1
    for a in range(10):
        f_num[str(a)] = 1
    print(find(s,0,len(s),i))

