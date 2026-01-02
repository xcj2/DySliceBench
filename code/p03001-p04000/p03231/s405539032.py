def gcd(a, b):
    big = max(a, b)
    small = min(a, b)
    
    r = small
    while r != 0:
        r = big % small
        big = small
        small = r
    
    return big
    
def lcm(a, b):
    gcd_num = gcd(a, b)
    return (a // gcd_num) * (b // gcd_num) * gcd_num

def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    
    a = n // gcd(n, m)
    b = m // gcd(n, m)
    lcm_num = lcm(n, m)
    
    ans = lcm_num
    for i in range(n // a):
        if s[a * i] != t[b * i]:
            ans = -1
            break
    
    print(ans)
    
if __name__ == '__main__':
    main()