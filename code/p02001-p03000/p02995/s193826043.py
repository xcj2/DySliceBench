
def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd_core(b, a % b)


def gcd(arr):
    g = gcd_core(arr[0], arr[1])
    for i in range(2, len(arr)):
        g = gcd_core(g, arr[i])
    return g

a,b,c,d = map(int,input().split())

def count(n,c,d):
    cn = n//c
    dn = n//d
    lcm = c*d//(gcd_core(c,d))
    both = n // lcm
    if lcm == c:
        # print("1")
        # print(cn, dn, both)
        return dn
    elif lcm == d:
        # print("2")
        # print(cn, dn, both)
        return cn
    else:
        # print("3")
        # print(cn,dn,both)
        return cn+dn-both

l = a-1-count(a-1,c,d)
r = b-count(b,c,d)
# print(l)
# print(r)

print(r-l)

