import sys
from collections import defaultdict
def smin(x,y):
    if x>y:
        return y
    else:
        return x

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())

    dd = defaultdict(list)
    ans = 10**27

    for i in range(N):
        x,y,u = input().split()
        x,y = int(x),int(y)
        dd[u].append((x,y))

    dd_u = defaultdict(list)

    for x,y in dd["U"]:
        dd_u[x].append((y,"U"))

    for x,y in dd["D"]:
        if x in dd_u:
            dd_u[x].append((y,"D"))

    for x in dd_u:
        dd_u[x].sort()
        for i in range(len(dd_u[x])-1):
            if dd_u[x][i][1]=="U" and dd_u[x][i+1][1]=="D":
                ans = smin((dd_u[x][i+1][0]-dd_u[x][i][0])/2,ans)

    dd_l = defaultdict(list)

    for x,y in dd["L"]:
        dd_l[y].append((x,"L"))

    for x,y in dd["R"]:
        if y in dd_l:
            dd_l[y].append((x,"R"))

    for y in dd_l:
        dd_l[y].sort()
        for i in range(len(dd_l[y])-1):
            if dd_l[y][i][1]=="R" and dd_l[y][i+1][1]=="L":
                ans = smin((dd_l[y][i+1][0]-dd_l[y][i][0])/2,ans)

    dd_v = defaultdict(list)

    for x,y in dd["U"]:
        v = y-x
        dd_v[v].append((x+y,"U"))

    for x,y in dd["L"]:
        v = y-x
        if v in dd_v:
            dd_v[v].append((x+y,"L"))

    for v in dd_v:
        dd_v[v].sort()
        for i in range(len(dd_v[v])-1):
            if dd_v[v][i][1]=="U" and dd_v[v][i+1][1]=="L":
                ans = smin((dd_v[v][i+1][0]-dd_v[v][i][0])/2,ans)

    dd_v = defaultdict(list)

    for x,y in dd["U"]:
        v = y+x
        dd_v[v].append((x-y,"U"))

    for x,y in dd["R"]:
        v = y+x
        if v in dd_v:
            dd_v[v].append((x-y,"R"))

    for v in dd_v:
        dd_v[v].sort()
        for i in range(len(dd_v[v])-1):
            if dd_v[v][i][1]=="R" and dd_v[v][i+1][1]=="U":
                ans = smin((dd_v[v][i+1][0]-dd_v[v][i][0])/2,ans)


    dd_v = defaultdict(list)

    for x,y in dd["D"]:
        v = y-x
        dd_v[v].append((x+y,"D"))

    for x,y in dd["R"]:
        v = y-x
        if v in dd_v:
            dd_v[v].append((x+y,"R"))

    for v in dd_v:
        dd_v[v].sort()
        for i in range(len(dd_v[v])-1):
            if dd_v[v][i][1]=="R" and dd_v[v][i+1][1]=="D":
                ans = smin((dd_v[v][i+1][0]-dd_v[v][i][0])/2,ans)

    dd_v = defaultdict(list)

    for x,y in dd["D"]:
        v = y+x
        dd_v[v].append((x-y,"D"))

    for x,y in dd["L"]:
        v = y+x
        if v in dd_v:
            dd_v[v].append((x-y,"L"))

    for v in dd_v:
        dd_v[v].sort()
        for i in range(len(dd_v[v])-1):
            if dd_v[v][i][1]=="D" and dd_v[v][i+1][1]=="L":
                ans = smin((dd_v[v][i+1][0]-dd_v[v][i][0])/2,ans)

    if ans>10**24:
        print("SAFE")
    else:
        print(int(ans*10))


if __name__ == '__main__':
    main()


