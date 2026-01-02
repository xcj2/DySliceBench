n,q = map(int,input().split())
s = input()
l = [list(input().split()) for i in range(q)]

def rb(x):
    st = x
    for i in range(q):
        if st == n:
            return True
        if st == -1:
            return False
        if l[i][0] == s[st]:
            if l[i][1] == "R":
                st += 1
            else:
                st -= 1
    if st == n:
        return True
    return False
def lb(x):
    st = x
    for i in range(q):
        if st == -1:
            return True
        if st == n:
            return False
        if l[i][0] == s[st]:
            if l[i][1] == "R":
                st += 1
            else:
                st -= 1
    if st == -1:
        return True
    return False
def bs():
    p = n
    ng = -1
    while abs(p - ng) > 1:
        m = (p+ng)//2
        if rb(m):
            p = m
        else:
            ng = m
    return p
def bs2():
    p = -1
    ng = n
    while abs(p-ng) > 1:
        m = (p+ng)//2
        if lb(m):
            p = m
        else:
            ng = m
    return p
print(bs() - bs2() -1)


