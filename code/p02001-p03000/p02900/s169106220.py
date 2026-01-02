def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n%i == 0:
            return False
    return True

def factors(N): #約数を全て求める。ただし、順不同
    from collections import deque
    ret = 0
    middle = int( N**(1/2))
    for i in range(1, middle):
        if N%i == 0:
            if is_prime(i):
                ret += 1
            if is_prime(N//i):
                ret += 1
            
    if N%middle == 0:
        if is_prime(middle):
            ret += 1
        if middle != N//middle:
            if is_prime(N//middle):
                ret += 1
    return ret

    
def main():
    a, b = map( int, input().split())
    d = gcd(a,b)
#    print(2, is_prime(2))
    if d == 1:
        print(1)
        return
    if is_prime(d):
        print(2)
        return

    print(factors(d)+1)

if __name__ == '__main__':
    main()