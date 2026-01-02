MAX = 100005
ws = [0 for i in range(MAX)] 
par = [-1 for i in range(MAX*2)]


def weight(x):
    root(x)
    return ws[x]

def root(x):
    if par[x] < 0: return x
    p = root(par[x])
    ws[x] = ws[x] + ws[par[x]]
    par[x] = p
    return par[x]


def unite(y, x, z):
    z = z + weight(x)
    z = z - weight(y)
    x = root(x)
    y = root(y)
    if x == y: return 0
    if par[y] < par[x]:
        tmp = x
        x = y 
        y = tmp 
        z = -z
     
    par[x] = par[x] + par[y]
    par[y] = x
    ws[y] = z
    return 1 

def diff(x,y):
    if root(x) != root(y) :return 0
    ans = ws[x] - ws[y]
    return 1 ,ans


if __name__=='__main__':
   global ans
   N, Q =  (int(x) for x in  input().split())
   for q in range(Q):
        t, *cmd =  (int(x) for x in  input().split())
        if t:
            x, y = cmd
            z = diff(x, y)
            if z==False :print("?")
            else :print(z[1])
        else:
            x, y, z = cmd
            unite(x, y, z)


