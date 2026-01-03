import sys


input = sys.stdin.readline




def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())



mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact



def serch(x, count):
    #print("top", x, count)
            

    for d in directions:
        nx = d+x
        #print(nx)
        if np.all(0 <= nx) and np.all(nx < (H, W)):
            if field[nx[0]][nx[1]] == "E":
                count += 1 
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)  
                continue
            if field[nx[0]][nx[1]] == "#":
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)    
                 
    return count

N=II()

t=acinput()
a=acinput()

st = [[] for i in range(N)]
st[0]=[t[0],t[0]]
for i in range(1,N):
    if t[i-1]<t[i]:
        st[i]=[t[i],t[i]]
    else:
        st[i]=[1,st[i-1][1]]
        

sa = [[] for i in range(N)]
sa[N-1] = [a[N-1], a[N-1]]
for i in reversed(range(N-1)):
    if a[i] > a[i+1]:
        sa[i] = [a[i], a[i]]
    else:
        sa[i] = [1,sa[i+1][1]]

def diff(x):
    return x[1]-x[0]
res=1
for i in range(N):
    
    x=max(sa[i])-min(st[i])+1
    y=max(st[i])-min(sa[i])+1
    #print(x,y,np.diff(sa))
    if x<=0 or y<=0:
        res=0
        break
    res=res* min(x,y,diff(sa[i])+1,diff(st[i])+1)
    res=res%mod
    
print(res%mod)

#print(st)
#print(sa)
