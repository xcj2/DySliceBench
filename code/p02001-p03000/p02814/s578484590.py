def lcm(a, b):
    return a * b // gcd(a, b)
    
    
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    base = 2
    while A[0] % (base*2) == 0:
        base *= 2
    minimum = 1
    for a in A:
        if a % base != 0 or (a // base) % 2 == 0:
            print(0)
            return
        minimum = lcm(minimum, a//base)
        if minimum > M:
            print(0)
            return
    minimum *= base // 2
    ans = (M // minimum + 1) // 2
    print(ans)
        

if __name__ == '__main__':
    main()