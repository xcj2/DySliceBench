import sys
input = sys.stdin.readline
n=int(input())
k=int(input())

def sol1(n):
    l=len(str(n))
    #print(int(str(n)[0])+9*(l-1))
    return int(str(n)[0])+9*(l-1)

def sol2(n):
    ret=0
    a=int(str(n)[0])
    l=len(str(n))-1
    ret+=sol1(n-a*10**l)
    ret+=(a-1)*sol1(10**l-1)
    ret+=9*9*l*(l-1)//2
    return ret

def sol3(n):
    ret=0
    a=int(str(n)[0])
    l=len(str(n))-1
    ret+=sol2(n-a*10**l)
    ret+=(a-1)*sol2(10**l-1)
    ret+=9*9*9*l*(l-1)*(l-2)//6
    return ret


if k==1:
    print(sol1(n))
elif k==2:
    print(sol2(n))
elif k==3:
    print(sol3(n))
