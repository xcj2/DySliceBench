def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b        
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def get_t(n):
    t = 0
    while n % 2 == 0:
        n //= 2
        t += 1
    return t


def main():
    n, m = map(int, input().split())
    a = [int(i) // 2 for i in input().split()]
    
    t = get_t(a[0])
    l = a[0] // 2**t
    m //= 2**t
    for i in range(1, len(a)):
        count = get_t(a[i])
        if count != t:
            return 0         

        l = lcm(a[i] // 2**t, l)
        if l > m:
            return 0
    
    m //= l
    ans = (m + 1) // 2
    
    return ans       
   

if __name__ == '__main__':
    ans = main()
    print(ans)