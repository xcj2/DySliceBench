def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a


import random
def is_prime(q, k=50):
    q = abs(q)
    if q == 2:
        return True
    if q < 2 or q % 2 == 0:
        return False

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t & 1 == 0:
            return False
    return True

def prime_num(target):
    ra = 2
    prime = 0
    while target>1:
        if target%ra == 0:
            prime += 1
            while target%ra==0:
                target = target//ra
            if is_prime(target):
                prime += 1
                break
        if ra == 2:
            ra += 1
        else:
            ra += 2
    return prime   
        
a, b = map(int, input().split())
gcd = xgcd(a, b)
if gcd == 1:
    print(1)
elif is_prime(gcd):
    print(2)
else:
    ans = prime_num(gcd)    
    print(ans+1)