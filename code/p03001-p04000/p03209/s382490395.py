n, x = [int(i) for i in input().split()]

def tlen(L):
    l = 1
    for i in range(1, L):
        l = l*2 + 3
    return l

def tpat(L):
    p = 1
    for i in range(1, L):
        p = p*2 + 1
    return p

def maisu(n, x):
    tl = tlen(n)
    if x == 1:
        return(0)
    elif n == 1:
        b = "bpppb"
        b = b[:x]
        return(b.count("p"))
    elif 2 <= x <= 1+tl-1:
        return(maisu(n-1, x-1))
    elif x == 1+tl:
        return(tpat(n))
    elif x == 2+tl:
        return(tpat(n)+1)
    elif tl+3 <= x <= 1+tl*2:
        return(tpat(n)+1+maisu(n-1,x-2-tl))
    else:
        return(tpat(n)*2+1)  

print(maisu(n,x))