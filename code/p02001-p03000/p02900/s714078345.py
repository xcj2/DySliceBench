a,b = map(int,input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def cf(x1,x2):
    cf=[]
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

ld=divisor(gcd(a,b))
ld.sort()
#ld.append(1)

#ld2 = divisor(gcd(a,b))
cnt=0
#print(ld)
ansl=[]
for i in ld:
    flg=0
    for j in ansl:
        #if i==j or i==1:
        #    break
        if gcd(i,j) !=1:
            flg = 1
            #print('flg',i,j)
            #if j in ld:
            #    print('in',i,j,gcd(i,j))
            #    ld.remove(j)
            break
        #print(i,j,gcd(i,j))
    if flg == 0:
        ansl.append(i)
    #print(ansl)


print(len(ansl))

#print(ld)