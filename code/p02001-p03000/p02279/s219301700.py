def Get_leafs_list(T, p):
    l = p.l
    ans = []
    while(T[l].r != -1):
        ans.append(T[l].r)
        l = T[l].r
    return ans

def rec(T,node, p):
    T[node].d = p
    if(T[node].r != -1):
        rec(T,T[node].r, p)
    if(T[node].l != -1):
        rec(T,T[node].l, p+1)


class Node():
    def __init__(self,i):
        self.p = -1
        self.l = -1
        self.r = -1
        self.d = 0
        self.n = i

    def Get_leafs_list(self,T):
        l = self.l
        if l != -1:
            ans = [l]
        else:
            ans = []
        while(T[l].r != -1):
            ans.append(T[l].r)
            l = T[l].r
        return ans


    def print_ans(self):
        print("node",self.n, end=": ")
        print("parent =",self.p, end=", ")
        print('depth =',self.d, end=", ")
        if self.l == -1 and self.p != -1:
            print('leaf, []')
            return
        else:
            if self.p == -1:
                print("root",end=", ")
            else :
                print("internal node",end=", ")
            ans = self.Get_leafs_list(T)
            print(ans)
T = []
n = int(input())
for i in range(0,n):
    T.append(Node(i))

for i in range(0,n):
    data = [int(x) for x in input().split()]
    k = data[0]
    if(data[1] != 0):   # node has leafs
        for j in range(0,data[1]):  #leafs
            if j == 0:
                T[k].l = data[2]
            else:
                T[l].r = data[2+j]
            l = data[2+j]
            T[l].p = data[0]
#get root 
for x in range(0,n):
    if(T[x].p == -1):
        root = x
        break
try:
    rec(T,root,0)

except:
    for i in range(1,n):
        T[i].d = 1

for x in T:
    x.print_ans()