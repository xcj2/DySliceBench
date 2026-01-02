def i_sort(l,g):
    cnt=0
    for i in range(g,len(l)):
        x=l[i]
        j=i
        while(0 <= j-g and l[j-g] > x):
            l[j-g],l[j]=l[j],l[j-g]
            j-=g
            cnt+=1
    return cnt


def mk_G(l):
    G=[1]
    i=0
    while(1):
        if(len(l) <= 3*G[i] +1):
            break
        G.append(3*G[i]+1)
        i+=1
    G.reverse()
    return G

def shell_sort(l,G):
    cnt=0
    if(len(l)!=1):
        for i in G:
            cnt+=i_sort(l,i)
    return cnt
        
        





n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))

G=mk_G(A)

count=shell_sort(A,G)

print(len(G))
print(" ".join(list(map(str,G))))
print(count)
for i in A:
    print(i)
