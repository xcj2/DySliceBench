import sys,collections,math,random;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

n_a = I()
As = [0]
for i in range(n_a):
    n_t = I()
    Ts = []
    for j in range(n_t):
        Ts.append(Is())
    As.append(Ts)

cand = []
def dfs(i,st):
    if i < n_a:
        dfs(i+1,st+[i+1])
        dfs(i+1,st)
    elif i == n_a:
        flag = True
        tf = [None] * (n_a + 1)
        for j in range(1,n_a+1):
            if j in st:
                tf[j] = 1
            else:
                tf[j] = 0
        for j in range(1,n_a+1):
            if j not in st:
                continue
            for e in As[j]:
                x,y = e
                if tf[x] != y:
                    #print("false",i,tf,st)
                    flag = False
        if flag:
            #print("true",i,tf,st)
            cand.append(tf)
dfs(0,[])
ans = 0
for e in cand:
    ans = max(ans,e.count(1))
print(ans)