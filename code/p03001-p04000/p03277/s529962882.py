
def bitadd(a,w,bit): #aにwを加える(1-origin)
 
    x = a
    while x <= (len(bit)-1):
        bit[x] += w
        x += x & (-1 * x)
 
def bitsum(a,bit): #ind 1～aまでの和を求める
 
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret


def updiv(a,b):
    if a % b == 0:
        return a//b
    else:
        return a//b +1

def want(x):

    lis = []
    for i in a:
        if i >= x:
            lis.append(1)
        else:
            lis.append(-1)

    slis = [0]
    for i in lis:
        slis.append(slis[-1] + i)

    #座圧する(1-Originにすべき)
    dic = {}
    nlis = []
    for i in slis:
        if i not in dic:
            dic[i] = None
            nlis.append(i)
    nlis.sort()
    for i in range(len(nlis)):
        dic[nlis[i]] = i+1

    #print (x,dic)
    
    ans = 0
    BIT = [0] * (len(nlis) + 1)

    for i in slis:
        j = dic[i]

        ans += bitsum(j,BIT)
        bitadd(j,1,BIT)
        
    #print (x,ans,slis)
    return ans
    

N = int(input())

a = list(map(int,input().split()))

l = 1
r = max(a) + 1

while r-l != 1:

    m = (l+r) // 2

    mnum = want(m)

    if mnum >= updiv((N**2+N)//2,2):
        l = m
    else:
        r = m

print (l)
