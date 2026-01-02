# E
B, W = map(int, input().split())

LARGE = 10**9 + 7

# pre compute
modulo = [0]*(2*10**5+1)
modulo[0] = 1
for i in range(1, 2*10**5+1):
    modulo[i] =(5*10**8 + 4) * modulo[i-1] % LARGE

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m    
    
frac_mod = [0]*(2*10**5+1)
frac_inv_mod = [0]*(2*10**5+1)
frac_mod[0] = 1
frac_inv_mod[0] = 1
frac_mod[1] = 1
frac_inv_mod[1] = 1

for i in range(2, 2*10**5+1):
    frac_mod[i] = frac_mod[i-1]*i % LARGE
    frac_inv_mod[i] = frac_inv_mod[i-1]*modinv(i, LARGE) % LARGE

B_lost_list = [0]*(B+W)
W_lost_list = [0]*(B+W)

def nCk_mod(n, k):
    return frac_mod[n]*frac_inv_mod[k]*frac_inv_mod[n-k] % LARGE

for n in range(B, B+W):
    B_lost_list[n] = nCk_mod(n-1, B-1)*modulo[n]
    
for n in range(W, B+W):
    W_lost_list[n] = nCk_mod(n-1, W-1)*modulo[n]
    
# must be B
b = 0
w = 0
for i in range(B+W):
    b = (b + B_lost_list[i]) % LARGE
    w = (w + W_lost_list[i]) % LARGE
    
    print((500000004 + w * 500000004 - b * 500000004) % LARGE)