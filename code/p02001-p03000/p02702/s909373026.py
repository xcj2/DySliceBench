def egcd(a, b):
    """Returns a triple (g, x, y), such that ax + by = g = gcd(a,b).
       Assumes a, b >= 0, and that at least one of them is > 0.
       Bounds on output values: |x|, |y| <= max(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m

def main():
    s = input()
    n = len(s)
    h = [0]
    for i in range(n):
        h.append((h[-1] * 10 + int(s[i])) % 2019)
    p = [1]
    for i in range(n):
        p.append((p[-1] * 10) % 2019)
    lk = {0 : 1}
    cnt = 0
    for i in range(1, len(h)):
        curr = (h[i] * modinv(p[i], 2019)) % 2019
        # print(i, curr)
        if curr in lk:
            cnt += lk[curr]
            lk[curr] += 1
        else:
            lk[curr] = 1 
    print(cnt)
    
if __name__ == '__main__':
    main()   
        