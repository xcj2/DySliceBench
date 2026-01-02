def readinput():
    n = int(input())
    s = list(map(int,input().split()))
    q = int(input())
    t = list(map(int,input().split()))
    return n,s,q,t

def main(n,s,q,t):
    c = 0
    for j in t:
        for i in s:
            if(i == j):
                c += 1
                break

    return c

def main2(n,s,q,t):
    c=0
    for tj in t:
        s.append(tj)
        i=0
        while(s[i]!=tj):
            i+=1
        if(i<n):
            c+=1
        s.pop()
    return c

def main3(n,s,q,t):
    sets = set(s)
    sett = set(t)
    return (len((sets & sett)))

if __name__=='__main__':
    n,s,q,t = readinput()
    ans = main3(n,s,q,t)
    print(ans)

