a = int(input())
x = list(map(int,input().split()))
ax = list(set(x))
x.sort()
ax = list(set(x))
def ch(l):
    # print(l,l[1:] + [l[0]], l[2:] + [l[0]] +[l [1]])
    for i, j ,k in zip(l,l[1:] + [l[0]], l[2:] + [l[0]] +[l [1]]):
        if j != i ^ k: break
    else:
        return(1)
    return(0)
def Y(a,t = 0):
    if a==t : print('YES')
    else : print('NO')
def y(a, t =0):
    if a==t : print('Yes')
    else : print('No')
if len(ax) < 3:
    if (sum(x) == 0) :
        print("Yes")
        exit()
    if (len(ax)) <2:
        print("No")
        exit()
    if x.count(0)*2 == x.count(ax[1]) and len(x) == x.count(0) + x.count(ax[1]):
        print("Yes")
        exit()
        
    print("No")
    exit()
t = (len(x) == x.count(ax[0]) + x.count(ax[1]) + x.count(ax[2])) * (x.count(ax[1]) == x.count(ax[0]) and x.count(ax[0]) == x.count(ax[2]))*ch(ax)

y(1,t)