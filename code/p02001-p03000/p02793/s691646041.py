n = int(input())

a = list(map(int, input().split()))

M = 1000000007


def mod(a, b):
    return (a % b + b) % b

def gcd(a ,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a,b) * b

def extGCD(a,b):
    if b==0:
        return a,1,0
    d, y, x = extGCD(b, a%b)
    y -= a // b * x
    return d, x, y

def modinv(a,p):
    b, x, y = extGCD(a, p)
    return mod(x,p)


gcdval = a[0]
modpi = 1
lcmval = 1
for i in range(n):
    modpi = mod(modpi * a[i], M)
    gcdval = gcd(gcdval, a[i])
    lcmval = lcm(lcmval, a[i])

#print("GCD: {}".format(gcdval))
#print("pi: {}".format(modpi))    
#print("lcm: {}".format(lcmval))

sum = 0
for i in range(n):
    sum = sum + mod(lcmval * modinv(a[i], M), M)
    #print("{}".format(mod(lcmval * modinv(a[i], M), M)))
    sum = mod(sum, M)

print("{}".format(sum))
