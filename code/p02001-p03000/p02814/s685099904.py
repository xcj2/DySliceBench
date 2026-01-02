
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b

def lcms(a):
    l = a[0]
    for num in a[1:]:
        l = lcm(l, num)
    return l

n, m = map(int, input().split())
a = list(map(int, input().split()))
# a2 = [num//2 for num in a]
acount = [None]*n # aを2で割れる回数
anum = [None]*n # 割ったあとの残り(=奇数)
for i,num in enumerate(a):
    c = 0
    while num%2==0 and num>1:
        num //=2
        c += 1
    acount[i] = c
    anum[i] = num
if all(item==acount[0] for item in acount):
    l = lcms(anum)
    num0 = l * (pow(2, (acount[0]-1)))
    span = num0*2
    if m<num0:
        print(0)
    else:
        print(int((m-num0)//span + 1))
else:
    print(0)