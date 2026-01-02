def M(x,L):
    l = list(str(x))
    while(len(l) != L):
        l.append("0")
    res = ""
    l.sort()
    for i in range(len(l)):
        res += l[len(l)-1-i]
    return int(res)

def m(x,L):
    l = list(str(x))
    while(len(l) != L):
        l.append("0")
    res = ""
    l.sort()
    for i in range(len(l)):
        res += l[i]
    return int(res)

def solve(a,L):
    checked = [-1 for i in range(1000000)]
    for i in range(30):
        if(checked[a] != -1):
            print(checked[a],a,i-checked[a])
            return
        checked[a] = i
        a = M(a,L) - m(a,L)

while(True):
    a,L = map(int,input().split())
    if(a == 0 and L == 0):
        break
    solve(a,L)
