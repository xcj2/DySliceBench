import math , sys

N  = int( input() )

A = list(map(int, input().split() ) )

def Prime(x):
    ub=int(math.sqrt(x))+2
    if x==2 or x==3 or x==5 or x==7:
        return True
    for i in range(2,ub):
        if x%i==0:
            return False
    return True

y = N
while not Prime(y):
    y+=1

def h1(x):
    return x % y
def h2(x):
    return 1+ x%(y-1)
def h(x,i):
    return (h1(x) + i*h2(x)) % y

def insert(T,x):
    i=0
    while True:
        j=h(x,i)
        if T[j][0]== -1:
            T[j][0]=x
            T[j][1]=1
            return j
        elif x ==T[j][0]:
            T[j][1]+=1
            return j
        else:
            i+=1

def search(T,x):
    i=0
    while True:
        j=h(x,i)
        if T[j][0] == x:
            return T[j][1]
        elif T[j][0] == -1:
            return -1
        else:
            i+=1

T = [[-1,0] for _ in range(y)]
for i in range(N):
    insert(T , i + A[i])
ans =0
        
for j in range(N):
    if j - A[j]>=0:
        s = search(T, j - A[j])
        if s >=0:
            ans+=s
print(ans)