def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    v = 0
    for i in range(l):
        h[i+1] = v = (v * base + ord(s[i])) % mod
    return h
def setup_pw(l):
    pw = [1]*(l + 1)
    v = 1
    for i in range(l):
        pw[i+1] = v = v * base % mod
    return pw
def get(h, b, l, r):
    return (h[r] - h[l] * b[r-l]) % mod

def check_bisect(l,h1,b1,h2,b2):
    for j in range(N-2*l+1):
        a1 = get(h1,b1,j,l+j)
        a2 = get(h2,b2,j,l+j)
        for k in range(N-2*l-j+1):
            if a1 == get(h1,b1,j+l+k,2*l+j+k) and a2 == get(h2,b2,j+l+k,2*l+j+k):
                return True
    return False

N = int(input())
S = input()
mod = 1000000007
base = 37
h1 = rolling_hash(S)
b1 = setup_pw(N)
base = 401
h2 = rolling_hash(S)
b2 = setup_pw(N)
left = 1
right = N // 2
finish = False
if N <= 26:
    s = set(list(S))
    if N <= 3:
        if len(s) < N:
            print('1')
        else:
            print('0')
        finish = True
    else:
        if len(s) == N:
            print('0')
            finish = True
while finish == False:
    if left == right:
        print(left)
        finish = True
    elif right - left == 1:
        if check_bisect(right,h1,b1,h2,b2):
            print(right)
        else:
            print(left)
        finish = True
    else:
        mid = (left+right) // 2
        if check_bisect(mid,h1,b1,h2,b2):
            left = mid
        else:
            right = mid - 1