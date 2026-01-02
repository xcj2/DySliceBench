n, m = [ int(v) for v in input().split() ]
a_list = [ int(v) for v in input().split() ]

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b >= 1:
        a, b = b, a % b
    return a
def lcm(a,b):
	return a * b // gcd(a,b)

def p2(x):
    ans = 0
    while x % 2 == 0:
        ans += 1
        x //= 2
    return ans

n = len(a_list)

p2_list = [p2(i) for i in a_list]

p2_set = set(p2_list)
if len(p2_set) != 1:
    print(0)
else:
    p = 1
    for i in a_list:
        p = lcm(p, i//2)
        if p > m:
            print(0)
            break
    if p <= m:
        m -= p
        print(m//(p*2)+1)