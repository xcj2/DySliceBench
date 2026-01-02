N,A,B,C,D=map(int,input().split())
s=list('.'+input())
def ren(start,end):
    count=0
    MAX=0
    for k in range(start,end+1):
        if s[k]==".":
            count+=1
            MAX=max(count,MAX)
        else:
            count=0
    return MAX>=3


def S(snuke,c):
    while snuke<=c and s[snuke]==".":
        if snuke==c:
            return True
        if s[snuke+1]=='#':
            snuke+=2
        else:
            snuke+=1
    return False

def H(hnuke,d):
    while hnuke<=d and s[hnuke]==".":
        if hnuke==d:
            return True
        if s[hnuke+1]=='#':
            hnuke+=2
        else:
            hnuke+=1
    return False


x=S(A,C)
y=H(B,D)

if (B<A and C<D):
    z= x and y and ren(A-1,C+1)

elif (A<B and D<C):
    z= x and y and ren(B-1,D+1)
else:
    z= x and y
print("Yes" if z else "No")