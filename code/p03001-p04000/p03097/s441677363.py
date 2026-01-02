def bit_remove(x,bit):
    return ((x>>(bit+1))<<bit)+(x%(1<<bit))
def bit_insert(x,bit,i):
    return ((x>>bit)<<(bit+1))+(i<<bit)+(x%(1<<bit))

def solve(n,a,b):
    if n==1:
        return [a,b]
    for bit in range(n):
        if (a^b)&(1<<bit):
            break
    c,d=bit_remove(a,bit),bit_remove(b,bit)
    L=list(map(lambda x: bit_insert(x,bit,(a>>bit)&1),solve(n-1,c,c^1)))
    R=list(map(lambda x: bit_insert(x,bit,(b>>bit)&1),solve(n-1,c^1,d)))
    return L+R

n,a,b=map(int,input().split())
if not bin(a^b).count('1')%2:
    print('NO')
else:
    print('YES')
    print(*solve(n,a,b))