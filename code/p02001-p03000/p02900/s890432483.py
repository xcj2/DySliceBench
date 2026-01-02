#a>b
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
#a>b
def lcm(a,b):
    return a*b // gcd(a,b)
def divisor(n):
    a = []
    root_n = int(n**0.5)
    for i in range(root_n):
        if n % (i+1) == 0:
            a.append(i+1)
            if (i+1) != n // (i+1):
                a.append(n//(i+1))
    a.sort()
    return a
A,B = map(int,input().split())
c = max(A,B)
d = min(A,B)
llcm = gcd(c,d)
yakus = divisor(llcm)

ans = 1
yak_flag = [1] * len(yakus)
for i in range(len(yakus)):
    if i == 0:
        continue
    k = yakus[i]
    if yak_flag[i] == 0:
        continue
    for j in range(i+1,len(yakus)):
        if yak_flag[j] == 0:
            continue
        if gcd(yakus[j],k) != 1:
            yak_flag[j] = 0
    ans += 1
print(ans)